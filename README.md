# Demo App

In this demo, we have some feature:

- An EventBridge Rule
- Two Lambda functions
- A AWS SQS Standard Queue

## Architecture

![](docs/architecture.png)

## Usage

To deploy this application:

```
sls deploy
```

_You can set the `stage` and `region` with the respective flags `--stage` and `--region`._

To remove the application:

```
sls remove
```

_If you used flags to deploy the application, you must use them again_

## References

![Integration between Serverless and SQS](https://www.serverless.com/blog/aws-lambda-sqs-serverless-integration)
![Serverless Roles per Function](https://www.serverless.com/plugins/serverless-iam-roles-per-function)
![Example on Several Lambda Functions app](https://github.com/sbstjn/sqs-worker-serverless)
![Serverless EventBridge Events](https://www.serverless.com/framework/docs/providers/aws/events/event-bridge/)
![Draw Architecture](https://aws.amazon.com/architecture/icons/)
