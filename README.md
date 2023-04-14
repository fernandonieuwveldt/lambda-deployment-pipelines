# AWS Lambda Project with Custom Layer and Modular Deployment Pipelines

This project demonstrates a modular approach to deploying an AWS Lambda function and custom layer using GitHub Actions. The custom layer can be used by multiple Lambda functions in your AWS account. The deployment pipelines are separated into individual YAML files, providing better modularity and separation of concerns.

## Folder Structure
```bash
├── LICENSE
├── README.md
├── cookiecutter.json
├── hooks
│   └── post_gen_project.py
└── {{cookiecutter.project_name}}
    ├── custom_layer
    │   ├── deploy_custom_layer.yml
    │   ├── layer_module.py
    │   └── layer_requirements.txt
    ├── lambda_container
    │   ├── Dockerfile
    │   ├── app.py
    │   └── deploy_lambda_container.yml
    ├── lambda_function
    │   ├── deploy_lambda_function.yml
    │   ├── lambda_function.py
    │   └── requirements.txt
    └── lambda_function_and_layer
        └── deploy_lambda_function_and_layer.yml
```

## Deployment Pipelines

There are four deployment pipelines to cater to different scenarios:

1. **Custom Layer Deployment (`deploy_custom_layer.yml`):** This pipeline deploys the custom layer independently, allowing you to update and manage the custom layer separately from the Lambda function. Useful when you need to update shared libraries or code used by multiple Lambda functions.

2. **Lambda Function Deployment (`deploy_lambda_function.yml`):** This pipeline deploys the Lambda function independently. Useful when you need to update the Lambda function code without modifying the custom layer.

3. **Lambda Function Deployment as Docker Container (`deploy_lambda_container.yml`):** This pipeline deploys the Lambda function using a Docker container. Useful when you want to package your Lambda function with a container image, which provides more flexibility in managing dependencies and runtime environment.

4. **Both Custom Layer and Lambda Function Deployment (`deploy_lambda_function_and_layer.yml`):** This pipeline deploys both the custom layer and the Lambda function together by utilizing the other two pipelines. Useful when you need to deploy updates to both components simultaneously.

## Custom Layer Dependencies

Update the `layer_requirements.txt` file with your custom layer's dependencies. The dependencies will be packaged with the custom layer and deployed to AWS Lambda during the GitHub Actions workflow.

## Lambda Function Dependencies

Update the `requirements.txt` file with your Lambda function's dependencies. The dependencies will be packaged with the Lambda function and deployed to AWS Lambda during the GitHub Actions workflow.

## Deployment

The deployment process is handled by GitHub Actions, which will automatically build and deploy the selected components when you push changes to the main branch. You can manually trigger the `deploy_custom_layer.yml`, `deploy_lambda_function.yml`, and `deploy_lambda_container.yml` workflows using the `workflow_dispatch` event.

To deploy your Lambda function using a Docker container, you can use the `deploy_lambda_container.yml` workflow. This workflow builds a Docker image containing your Lambda function code and dependencies, pushes the image to Amazon Elastic Container Registry (ECR), and deploys the Lambda function using the container image. This approach provides more flexibility in managing dependencies and the runtime environment of your Lambda function.


## Benefits of This Pipeline Approach

1. **Modularity:** The separation of the custom layer and Lambda function deployment pipelines allows for better organization and independent updates to either component.

2. **Flexibility:** The ability to deploy the custom layer or Lambda function independently caters to different scenarios and requirements, while the combined deployment pipeline ensures that both components can be deployed together when needed.

3. **Version control:** By using GitHub Actions in combination with your source code repository, you can keep track of changes to the custom layer, Lambda function, and their dependencies over time. This makes it easier to identify issues and roll back to previous versions if necessary.

4. **Collaboration:** A modular pipeline approach makes it easier for team members to collaborate on different aspects of the project, as they can contribute changes through pull requests and rely on the pipeline to automatically deploy the necessary components upon merging.

5. **Time-saving and consistency:** By automating the build and deployment process, developers can focus on writing code and improving the application, rather than spending time on manual deployment tasks. The pipelines also ensure consistent packaging and deployment of the components across different environments, reducing the risk of errors due to manual processes or misconfigurations.

## Using Cookiecutter

To use the Cookiecutter template with this project, follow these steps:

1. Install Cookiecutter: `pip install cookiecutter`
2. Run the Cookiecutter command: `cookiecutter https://github.com/yourusername/cookiecutter-lambda-custom-layer`
3. Fill in the prompted values to customize your project, such as project name, Lambda function name, custom layer name, and AWS account number.

When prompted, fill in the values for your project, such as project name, Lambda function name, custom layer name. Cookiecutter will generate a new folder structure within your larger project that includes the necessary deployment pipelines and source code folders for the Lambda function and custom layer.


Cookiecutter will create a new folder with the generated project structure, which you can then customize and use as needed.


## A note on the IAM user and role permissions

In your AWS account, create an IAM user with programmatic access and attach a policy with the required permissions to manage Lambda functions and layers. Store the AWS access key ID and secret access key as secrets in your GitHub repository with the names AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. Also need to add a AWS_ACCOUNT secret.

The following IAM policy should be attached to the IAM user the github actions is running on. This is the case for deploying lambda functions and custom layers.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "0",
            "Effect": "Allow",
            "Action": [
                "iam:ListRoles",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionCode",
                "lambda:PublishLayerVersion",
                "lambda:UpdateFunctionConfiguration",
                "lambda:DeleteLayerVersion",
                "lambda:UpdateLayerVersion",
                "s3:PutObject",
                "s3:GetObject",
                "s3:PutObjectAcl"
            ],
            "Resource": [
                "arn:aws:s3:::your-s3-bucket-name/*",
                "arn:aws:lambda:*:*:function:<your lambda function name>",
                "arn:aws:lambda:*:*:layer:<your custom layer name>",
                "arn:aws:lambda:*:*:layer:<your custom layer name>:*"
            ]
        }
    ]
}
```

An example for the IAM policy to deploy a lambda docker container. These are the minimum permissions you will need:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "0",
            "Effect": "Allow",
            "Action": [
                "iam:ListRoles",
                "ecr:CreateRepository",
                "ecr:DescribeRepositories",
                "ecr:GetAuthorizationToken",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage"
            ],
            "Resource": [
                "arn:aws:s3:::your-s3-bucket-name/*",
                "arn:aws:lambda:*:123456789012:function:<your lambda function name>",
                "arn:aws:lambda:*:123456789012:layer:<your custom layer name>",
                "arn:aws:lambda:*:123456789012:layer:<your custom layer name>:*",
                "arn:aws:ecr:*:123456789012:repository/<your ecr repository>"
            ]
        }
    ]
}

```

Finally, to create a new AWS Lambda function, the IAM role used to create the function should have permissions to perform the following actions:

* `lambda:CreateFunction` - this permission allows the role to create a new Lambda function.
* `lambda:UpdateFunctionCode` - this permission allows the role to update the code of an existing Lambda function.
* `lambda:UpdateFunctionConfiguration` - this permission allows the role to update the configuration of an existing Lambda function.

To grant these permissions to the IAM role, you can attach an appropriate IAM policy to the role. Here's an example policy that grants these permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:CreateFunction",
                "lambda:UpdateFunctionCode",
                "lambda:UpdateFunctionConfiguration"
            ],
            "Resource": "*"
        }
    ]
}
```
