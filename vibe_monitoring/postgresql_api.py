
import oci
config = oci.config.from_file("./config")

# Initialize service client with default config file
psql_client = oci.psql.PostgresqlClient(config)

db_system_id = "ocid1.postgresqldbsystem.oc1.eu-frankfurt-1.amaaaaaaeicj2tiai2hwxh3zksqcurqlwwc5cxxcenybecgyoxdw7upktikq"

# Restart Primary endpoint API
restart_db_instance_in_db_system_response = psql_client.restart_db_instance_in_db_system(
    db_system_id=db_system_id,
    restart_db_instance_in_db_system_details=oci.psql.models.RestartDbInstanceInDbSystemDetails(
        db_instance_id="71b27d10-8cb3-4ea3-85bb-e988a3949e92",
        restart_type="NORMAL"))


# Restart READ endpoint API
restart_db_instance_in_db_system_response = psql_client.restart_db_instance_in_db_system(
    db_system_id=db_system_id,
    restart_db_instance_in_db_system_details=oci.psql.models.RestartDbInstanceInDbSystemDetails(
        db_instance_id="34099b41-253a-4365-a64a-36edff6178fb",
        restart_type="NORMAL"))