from datetime import datetime
import oci

config = oci.config.from_file("./config")

monitoring_client = oci.monitoring.MonitoringClient(config)

#compartemnt id
compartment_id="ocid1.compartment.oc1..aaaaaaaalylfheeqdzzrarod4qkgqhmztthdk4djxcfgw65gdi2odd2lc3tq"
namespace="oci_postgresql"

#Metric 1 - Connections
summarize_metrics_data_response_metric_1 = monitoring_client.summarize_metrics_data(
    compartment_id=compartment_id,
    summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
        namespace=namespace,
        query="Connections[1m]{resourceId = \"ocid1.postgresqldbsystem.oc1.eu-frankfurt-1.amaaaaaaeicj2tiai2hwxh3zksqcurqlwwc5cxxcenybecgyoxdw7upktikq\"}.groupBy(dbInstanceId,dbInstanceRole).max()"
        ))


#Metric 2 - CPU Utilization
summarize_metrics_data_response_metric_2 = monitoring_client.summarize_metrics_data(
    compartment_id=compartment_id,
    summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
        namespace=namespace,
        query="CpuUtilization[1m]{resourceId=ocid1.postgresqldbsystem.oc1.eu-frankfurt-1.amaaaaaaeicj2tiai2hwxh3zksqcurqlwwc5cxxcenybecgyoxdw7upktikq}.groupBy(dbInstanceId,dbInstanceRole).mean()"
        ))


#Metric 3 - Memory Utilization
summarize_metrics_data_response_metric_3 = monitoring_client.summarize_metrics_data(
    compartment_id=compartment_id,
    summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
        namespace=namespace,
        query="MemoryUtilization[1m]{resourceId=ocid1.postgresqldbsystem.oc1.eu-frankfurt-1.amaaaaaaeicj2tiai2hwxh3zksqcurqlwwc5cxxcenybecgyoxdw7upktikq}.groupBy(dbInstanceId,dbInstanceRole).mean()"
        ))


#Metric 4 - Write IOPS
summarize_metrics_data_response_metric_4 = monitoring_client.summarize_metrics_data(
    compartment_id=compartment_id,
    summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
        namespace=namespace,
        query="WriteIops[1m]{resourceId=ocid1.postgresqldbsystem.oc1.eu-frankfurt-1.amaaaaaaeicj2tiai2hwxh3zksqcurqlwwc5cxxcenybecgyoxdw7upktikq}.groupBy(dbInstanceId,dbInstanceRole).mean()"
        ))


#Metric 5 - Read IOPS
summarize_metrics_data_response_metric_5 = monitoring_client.summarize_metrics_data(
    compartment_id=compartment_id,
    summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
        namespace=namespace,
        query="ReadIops[1m]{resourceId=ocid1.postgresqldbsystem.oc1.eu-frankfurt-1.amaaaaaaeicj2tiai2hwxh3zksqcurqlwwc5cxxcenybecgyoxdw7upktikq}.groupBy(dbInstanceId,dbInstanceRole).mean()"
        ))



# Get the data from response
print(summarize_metrics_data_response_metric_5.data)