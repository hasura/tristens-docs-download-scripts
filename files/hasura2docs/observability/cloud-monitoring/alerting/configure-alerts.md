# Configure Alerts

## Configuration​

You can easily configure alerts for your Hasura Cloud project on the Cloud Dashboard. Navigate to the `Project Detail -> Alerting` menu and enable the feature in just a few clicks.

In the screenshot below, we've toggled the `Enable Alert` option and added a single recipient's email address:

Image: [ Hasura Cloud alerting configuration ](https://hasura.io/docs/assets/images/alerting-config-f6d06a4d651c6c1df768d28fa1e4ae30.jpg)

## Alert Rules​

Hasura Cloud supports a set of common alert rules for performance observability such as:

- Metadata health
- High latency
- Error rates of GraphQL requests, subscriptions, and Event Triggers.


To choose which alerts you receive, click on `Configure Alerts` to open the configuration dialog:

Image: [ Alert rules configuration ](https://hasura.io/docs/assets/images/alerting-config-rules-ce36b9f8d9d44e976fb5e2746aaaf45f.png)

## Notification services​

### Email​

Email is the default service. You can add email addresses that you want to receive alert notifications:

Image: [ Alert email configuration ](https://hasura.io/docs/assets/images/alerting-config-email-d0bf281ec2a4fb45ead3fb098b22906a.png)

Once you have completed the configuration, you will start receiving alert emails containing the specified content
whenever there is any relevant information to be conveyed. An example is below:

Image: [ Alert email content ](https://hasura.io/docs/assets/images/alerting-email-template-c6dd7b9e2a457158c4d0ce681221d9a3.png)

### Slack​

To enable Slack notifications, click on `Sign in with Slack` to register the `Hasura Alert App` to your Slack workspace.
Then, choose the channel that you want Hasura to send alert notifications to and click `Allow` .

Image: [ Alert slack configuration ](https://hasura.io/docs/assets/images/alerting-config-slack-2b9ca00473c5d5a6cf0fb6681c276b88.png)

Once you have completed the configuration, you will start receiving Slack messages containing the specified content
whenever the alert is triggered. An example is below:

Image: [ Alert Slack content ](https://hasura.io/docs/assets/images/alerting-slack-template-dd7077830ed8c61095d71ce3817419c7.png)

### What did you think of this doc?

- [ Configuration ](https://hasura.io/docs/latest/observability/cloud-monitoring/alerting/configure-alerts/#configuration)
- [ Alert Rules ](https://hasura.io/docs/latest/observability/cloud-monitoring/alerting/configure-alerts/#alert-rules)
- [ Notification services ](https://hasura.io/docs/latest/observability/cloud-monitoring/alerting/configure-alerts/#notification-services)
    - [ Email ](https://hasura.io/docs/latest/observability/cloud-monitoring/alerting/configure-alerts/#email)

- [ Slack ](https://hasura.io/docs/latest/observability/cloud-monitoring/alerting/configure-alerts/#slack)


Image: [ Hasura Con ](https://res.cloudinary.com/dh8fp23nd/image/upload/v1677759444/main-web/Group_11455_2_rdpykm.png)

### Best Practices for API Observability with Hasura

### Start with GraphQL on Hasura for Free

- Build apps and APIs 10x faster
- Built-in authorization and caching
- 8x more performant than hand-rolled APIs


Image: [ Promo ](https://hasura.io/docs/assets/images/hasura-free-ff60e409244e0ea12b5a3045d1a9096b.png)