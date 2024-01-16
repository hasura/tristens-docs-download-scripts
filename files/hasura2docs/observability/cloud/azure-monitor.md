# Azure Monitor Integration on Hasura Cloud

## Introduction​

You can export metrics, operation logs and traces of your Hasura Cloud project to[ Azure Monitor ](https://azure.microsoft.com/en-in/services/monitor/). This can be configured on the integrations tab on
the project's setting page.

Note

For Hasura Cloud projects, the Azure Monitor Integration is only available on the `Standard` (pay-as-you-go) tier and
above.

More metrics on OpenTelemetry exporter

Try the new[ OpenTelemetry exporter ](https://hasura.io/docs/latest/observability/opentelemetry/)to get advanced metrics and traces to connect
with Azure Monitor. This integration will export the metrics as detailed[ here ](https://hasura.io/docs/latest/observability/cloud/azure-monitor/#view-metrics).

## Pre-requisites​

- Create a[ Service Principal ](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#register-an-application-with-azure-ad-and-create-a-service-principal)in Azure.
- From the `Overview` tab of the created Service principal, retrieve `Application (client) ID` (Referred as `Active Directory Client ID` in this context) and `Directory (tenant) ID` (Referred as `Active Directory Tenant ID` in
this context)
- From the `Certificates & secrets` tab of the created service principal, Create a client secret by clicking `New client secret` . Add a suitable description and expiry period for the secret and click `Add` . Copy the value of
the created secret (Referred to as `Active Directory Client Secret` in this context)
- Create a[ Log Analytics Workspace ](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/quick-create-workspace)in Azure.
- From the `Agents management` tab of the created log analytics workspace, retrieve `Workspace ID` and `Primary Key` (Referred as `Shared Key` in this context).
- From the `Properties` tab of the created log analytics workspace, retrieve `Resource ID` and `Location` (Referred to
as `Region` in this context)
- Assign the Role `Monitoring Metrics Publisher` to the Service principal against the Log analytics workspace. From the `Access control (IAM)` tab of the created log analytics workspace, Click on `Add` and select `Add role assignment` . In
the Add role assignment panel, Select the Role as `Monitoring Metrics Publisher` and select the created service
principal for role assignment and click `Save` .
- Create an[ Application Insights resource ](https://docs.microsoft.com/en-us/azure/azure-monitor/app/create-new-resource%3E)in
Azure.
- From the `Overview` tab of the created Application Insights resource, retrieve `Instrumentation Key`


Create a[ Service Principal ](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#register-an-application-with-azure-ad-and-create-a-service-principal)in Azure.

From the `Overview` tab of the created Service principal, retrieve `Application (client) ID` (Referred as `Active Directory Client ID` in this context) and `Directory (tenant) ID` (Referred as `Active Directory Tenant ID` in
this context)

Image: [ Service Principal Properties ](https://hasura.io/docs/assets/images/service-principal-properties-7b5534fde598749f456e114142aaa401.png)

From the `Certificates & secrets` tab of the created service principal, Create a client secret by clicking `New client secret` . Add a suitable description and expiry period for the secret and click `Add` . Copy the value of
the created secret (Referred to as `Active Directory Client Secret` in this context)

Image: [ Service Principal Secret ](https://hasura.io/docs/assets/images/service-principal-secret-3239782769d7ca710d5081405cf8f122.png)

Create a[ Log Analytics Workspace ](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/quick-create-workspace)in Azure.

From the `Agents management` tab of the created log analytics workspace, retrieve `Workspace ID` and `Primary Key` (Referred as `Shared Key` in this context).

Image: [ Log Analytics workspace config parameters ](https://hasura.io/docs/assets/images/log-analytics-workspace-config-d0b9fb0f01b81dce74e11774828595b1.png)

From the `Properties` tab of the created log analytics workspace, retrieve `Resource ID` and `Location` (Referred to
as `Region` in this context)

Image: [ Log Analytics Properties ](https://hasura.io/docs/assets/images/log-analytics-properties-045f1698db4a431eedb14d5c319b2339.png)

Assign the Role `Monitoring Metrics Publisher` to the Service principal against the Log analytics workspace. From the `Access control (IAM)` tab of the created log analytics workspace, Click on `Add` and select `Add role assignment` . In
the Add role assignment panel, Select the Role as `Monitoring Metrics Publisher` and select the created service
principal for role assignment and click `Save` .

Image: [ Service Principal Role ](https://hasura.io/docs/assets/images/service-principal-role-02e897d6784d2d97482566610dfd7da3.png)

Create an[ Application Insights resource ](https://docs.microsoft.com/en-us/azure/azure-monitor/app/create-new-resource%3E)in
Azure.

From the `Overview` tab of the created Application Insights resource, retrieve `Instrumentation Key` 

Image: [ Instrumentation Key ](https://hasura.io/docs/assets/images/azure-instrumentation-key-0a44a05eb86d4a7506a77d2d92fc4379.png)

## Configure Azure Monitor integration​

On the Project settings page, navigate to **Integrations > Azure Monitor** .

Image: [ Configure Azure Monitor Integration ](https://hasura.io/docs/assets/images/integrate-azure-monitor-28e1fef373f80fed24c28022cc7f52e3.png)

Enter the values of config parameters obtained from the steps in pre-requisites in the Azure monitor integration form.
In addition to the above parameters, the following fields are also needed:

| Field | Description |
|---|---|
| [ Namespace ](https://docs.microsoft.com/en-us/azure/azure-monitor/essentials/metrics-custom-overview#namespace) | Namespaces are a way to categorize or group similar metrics together. |
| [ Log type ](https://docs.microsoft.com/en-us/azure/azure-monitor/logs/data-collector-api#request-headers) | The record type of the log that is being submitted. It can contain only letters, numbers, and the underscore (_) character, and it can't exceed 100 characters. |
| Custom Attributes **(Optional)**  | Custom Attributes associated with your logs. A default source tag `hasura-logs` is added to all exported logs. |


After adding appropriate values in the Azure monitor Integration panel, click `Connect Integration` .

## Checking the status of the integration​

The green/red dot signifies the status of the integration. For each of the telemetry types (logs, metrics, traces) green
signifies successful exporting of the telemetry to Azure monitor. `Last Exported` is continuously updated, indicating
the timestamp of the last telemetry (log, metric, trace) successfully exported to your Azure monitor dashboard.

Image: [ Azure monitor Integration successfully configured ](https://hasura.io/docs/assets/images/configure-azure-monitor-done-7f6066a6ad740ab81116c9576d96c8b0.png)

In case of error while exporting any of telemetries(logs, metrics, traces) to Azure monitor, the dot becomes red and the
error messages/instructions are displayed. Click `Update Settings` button to update the config parameters.

Image: [ Azure monitor Integration unable to push logs ](https://hasura.io/docs/assets/images/configure-azure-monitor-fail-c2026187a8cfb8e03198bf9d7c71b095.png)

## View metrics​

The integration exports the following five metrics to Azure monitor:

| Metric Exported | Metric Name in Azure monitor |
|---|---|
| Average number of requests |  `average_ requests_ per_ minute`  |
| Average request execution time |  `average_ execution_ time`  |
| Success rate of requests |  `success_ rate`  |
| Active subscriptions |  `active_ subscriptions`  |
| Number of websockets open |  `websockets_ open`  |


Non-zero values of all the above metrics are exported over a minute time interval.

To navigate to[ Azure monitor metrics dashboard ](https://portal.azure.com/#blade/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/metrics),click `View Metrics` .

Image: [ Azure monitor Integration successfully configured ](https://hasura.io/docs/assets/images/azure-monitor-view-metrics-72d4b24825bc20506f8132feb7e95514.png)

From the `Select a scope` panel, expand the resource group which contains the `Log analytics workspace` and select it
and click `Apply` . In the filter menu, select the correct namespace and `Add filter` to view the individual metric.

Image: [ Metrics successfully exported to Azure monitor ](https://hasura.io/docs/assets/images/azure-monitor-metrics-94633a8f6595cf914da42082cf4ab5b1.png)

## View logs​

To navigate to[ Azure monitor logs dashboard ](https://portal.azure.com/#blade/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/logs),
click `View Logs` .

Image: [ Azure monitor Integration successfully configured ](https://hasura.io/docs/assets/images/azure-monitor-view-logs-c9079622b6fb67bcf74ea0c5c5907155.png)

From the `Select a scope` panel, expand the resource group which contains the `Log analytics workspace` and select it
and click `Apply` . The logs can be filtered using `Log type` . Use `{YOUR_LOG_TYPE}_CL` search parameter to filter the
logs. Custom log types are displayed in the left of the Query panel.

Image: [ Logs successfully exported to Azure monitor ](https://hasura.io/docs/assets/images/azure-monitor-logs-fb5e5c6a6c6c8b9fb6a22fb17e8e7387.png)

## View traces​

To navigate to[ Azure monitor traces dashboard ](https://portal.azure.com/#blade/Microsoft_Azure_Monitoring/AzureMonitoringBrowseBlade/applicationsInsights),
click `View traces` .

Image: [ Application Insights Instrumentation Key ](https://hasura.io/docs/assets/images/azure-monitor-view-traces-854ae3557656fa8de442fce7e7da55a8.png)

Select the appropriate `Application Insights` and click `Transaction search` . The traces can be filtered using `Trace` and `Dependency` Event types. Clicking any of the `Dependency` result shows the `End-to-end transaction details` for the
corresponding trace.

Image: [ Traces successfully exported to Azure monitor ](https://hasura.io/docs/assets/images/azure-monitor-trace-flame-graph-4e250be3e9fd59ee4415a73ce459c461.png)

### What did you think of this doc?

- [ Introduction ](https://hasura.io/docs/latest/observability/cloud/azure-monitor/#introduction)
- [ Pre-requisites ](https://hasura.io/docs/latest/observability/cloud/azure-monitor/#pre-requisites)
- [ Configure Azure Monitor integration ](https://hasura.io/docs/latest/observability/cloud/azure-monitor/#configure-azure-monitor-integration)
- [ Checking the status of the integration ](https://hasura.io/docs/latest/observability/cloud/azure-monitor/#checking-the-status-of-the-integration)
- [ View metrics ](https://hasura.io/docs/latest/observability/cloud/azure-monitor/#view-metrics)
- [ View logs ](https://hasura.io/docs/latest/observability/cloud/azure-monitor/#view-logs)
- [ View traces ](https://hasura.io/docs/latest/observability/cloud/azure-monitor/#view-traces)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759444/main-web/Group_11455_2_rdpykm.png)

### Best Practices for API Observability with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)