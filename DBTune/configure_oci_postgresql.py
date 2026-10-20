#!/usr/bin/env python3
"""Create an OCI PostgreSQL configuration and apply it with RESTART.

Install: python -m pip install oci

Required environment variables:
    OCI_COMPARTMENT_ID      Compartment in which to create the configuration.
    OCI_DB_SYSTEM_ID        Existing PostgreSQL DB-system OCID.

Optional environment variables (defaults in parentheses):
    OCI_CONFIG_FILE        API-key configuration file (~/.oci/config).
    OCI_CONFIG_PROFILE     Profile in that file (DEFAULT).
    OCI_REGION             Overrides the region in the configuration file.
    OCI_DB_VERSION         PostgreSQL version (17).
    OCI_CONFIG_NAME        New configuration display name (config_custom_v1).
    OCI_DB_SHAPE           Shape (VM.Standard.E6.Flex).
    OCI_WAIT_TIMEOUT       Timeout per waiting stage, seconds (3600).
    OCI_POLL_INTERVAL      Poll interval, seconds (10).
    PG_<CONFIG_KEY>        Override one of the 18 values in DEFAULT_OVERRIDES,
                           using an uppercase key, e.g. PG_WORK_MEM=8192.

Uses API-key signing from the selected OCI config profile. That profile must
contain user, tenancy, fingerprint, key_file, and region. No OCI CLI is needed.

Only the 18 listed PostgreSQL keys are submitted as overrides. Other parameters
come from OCI's default configuration; existing custom overrides are not copied.
Each invocation creates a new configuration. Its OCID is printed immediately.
If applying it fails, it is retained for inspection. A timeout does not cancel
an operation already accepted by OCI. Applying uses RESTART and can interrupt
database connections. Success means the work request succeeded and OCI reports
the DB system ACTIVE with the newly created config_id; SQL values are not queried.
"""

import json
import os
import sys
import time


DEFAULT_OVERRIDES = {
    "work_mem": "4096",
    "random_page_cost": "4",
    "seq_page_cost": "1",
    "checkpoint_completion_target": "1",
    "effective_io_concurrency": "1",
    "max_parallel_workers_per_gather": "3",
    "max_parallel_workers": "8",
    "max_wal_size": "1024",
    "min_wal_size": "1024",
    "bgwriter_lru_maxpages": "100",
    "bgwriter_delay": "200",
    "effective_cache_size": "3145728",
    "maintenance_work_mem": "65536",
    "default_statistics_target": "100",
    "max_parallel_maintenance_workers": "2",
    "shared_buffers": "851968",
    "max_worker_processes": "8",
    "wal_buffers": "-1",
}


def env(name, default=None):
    value = os.environ.get(name, default)
    if value is None or not value.strip():
        raise ValueError("Set a nonempty {} environment variable.".format(name))
    return value.strip()


def positive_int(name, default):
    value = int(env(name, str(default)))
    if value <= 0:
        raise ValueError("{} must be a positive integer.".format(name))
    return value


def wait_for(fetch, ready, failed, description, timeout, interval):
    """Poll a read API, stopping on success, terminal failure, or timeout."""
    deadline = time.monotonic() + timeout
    while True:
        resource = fetch().data
        if failed(resource):
            raise RuntimeError("{} failed: {}".format(description, resource))
        if ready(resource):
            return resource
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError(
                "Timed out waiting for {}. Check OCI before rerunning; "
                "accepted operations may still be running.".format(description)
            )
        time.sleep(min(interval, remaining))


def run(oci):
    # Validate all local input before making a mutation.
    compartment_id = env("OCI_COMPARTMENT_ID")
    db_system_id = env("OCI_DB_SYSTEM_ID")
    db_version = env("OCI_DB_VERSION", "17")
    display_name = env("OCI_CONFIG_NAME", "config_custom_v1")
    shape = env("OCI_DB_SHAPE", "VM.Standard.E6.Flex")
    timeout = positive_int("OCI_WAIT_TIMEOUT", 3600)
    interval = positive_int("OCI_POLL_INTERVAL", 10)
    overrides = {
        key: env("PG_" + key.upper(), value)
        for key, value in DEFAULT_OVERRIDES.items()
    }
    config = oci.config.from_file(
        file_location=os.path.expanduser(env("OCI_CONFIG_FILE", "~/.oci/config")),
        profile_name=env("OCI_CONFIG_PROFILE", "DEFAULT"),
    )
    if "OCI_REGION" in os.environ:
        config["region"] = env("OCI_REGION")
    oci.config.validate_config(config)
    client = oci.psql.PostgresqlClient(
        config, retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
    )

    # Catch wrong region/ID, incompatible shape/version, and busy systems early.
    db = client.get_db_system(db_system_id).data
    if db.lifecycle_state != "ACTIVE":
        raise RuntimeError("DB system must be ACTIVE; got {}.".format(db.lifecycle_state))
    if db.shape != shape:
        raise ValueError("OCI_DB_SHAPE={} does not match DB shape {}.".format(shape, db.shape))
    if db.db_version.split(".")[0] != db_version.split(".")[0]:
        raise ValueError("OCI_DB_VERSION={} does not match DB version {}.".format(db_version, db.db_version))

    models = oci.psql.models
    details = models.CreateConfigurationDetails(
        compartment_id=compartment_id,
        db_version=db_version,
        display_name=display_name,
        shape=shape,
        db_configuration_overrides=models.DbConfigurationOverrideCollection(
            items=[
                models.ConfigOverrides(
                    config_key=key,
                    # 'overriden' is the spelling required by the OCI SDK.
                    overriden_config_value=value,
                )
                for key, value in overrides.items()
            ]
        ),
    )
    print("Creating configuration {!r}...".format(display_name), flush=True)
    created = client.create_configuration(details).data
    config_id = created.id
    print("Created configuration OCID: {}".format(config_id), flush=True)
    wait_for(
        lambda: client.get_configuration(config_id),
        lambda item: item.lifecycle_state == "ACTIVE",
        lambda item: item.lifecycle_state in {"FAILED", "DELETING", "DELETED"},
        "configuration {} to become ACTIVE".format(config_id), timeout, interval,
    )

    # Refresh the ETag after creating the configuration to guard concurrent edits.
    current = client.get_db_system(db_system_id)
    if current.data.lifecycle_state != "ACTIVE":
        raise RuntimeError("DB system is no longer ACTIVE; new configuration retained.")
    update_kwargs = {}
    if current.headers.get("etag"):
        update_kwargs["if_match"] = current.headers["etag"]
    print("Applying {} to {} with RESTART...".format(config_id, db_system_id), flush=True)
    response = client.update_db_system(
        db_system_id,
        models.UpdateDbSystemDetails(
            db_configuration_params=models.UpdateDbConfigParams(
                apply_config="RESTART", config_id=config_id,
            )
        ),
        **update_kwargs
    )
    work_request_id = response.headers.get("opc-work-request-id")
    if not work_request_id:
        raise RuntimeError(
            "Update accepted without an opc-work-request-id; cannot confirm "
            "completion. Check the DB system in OCI before rerunning."
        )
    print("Update work request: {}".format(work_request_id), flush=True)
    wait_for(
        lambda: client.get_work_request(work_request_id),
        lambda item: item.status == "SUCCEEDED",
        lambda item: item.status in {"FAILED", "CANCELED"},
        "update work request {} (see OCI work-request errors for details)".format(work_request_id),
        timeout, interval,
    )
    updated = wait_for(
        lambda: client.get_db_system(db_system_id),
        lambda item: item.lifecycle_state == "ACTIVE" and item.config_id == config_id,
        lambda item: item.lifecycle_state in {"FAILED", "NEEDS_ATTENTION", "DELETING", "DELETED"},
        "DB system to become ACTIVE with configuration {}".format(config_id),
        timeout, interval,
    )
    print(json.dumps({
        "db_system_id": db_system_id,
        "config_id": updated.config_id,
        "lifecycle_state": updated.lifecycle_state,
        "work_request_id": work_request_id,
    }, indent=2))


def main():
    if len(sys.argv) == 2 and sys.argv[1] in {"-h", "--help"}:
        print(__doc__)
        return 0
    if len(sys.argv) != 1:
        print("Use environment variables for input; see --help.", file=sys.stderr)
        return 2
    try:
        import oci
    except ImportError:
        print("Install the OCI SDK: python -m pip install oci", file=sys.stderr)
        return 1
    try:
        run(oci)
    except Exception as exc:
        print("ERROR: {}".format(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
