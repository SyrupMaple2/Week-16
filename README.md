# Stop All EC2 Instances - AWS Lambda Project

## Description
This script is an AWS Lambda function to stop all running EC2 instances at a scheduled time to reduce costs.

## Steps to Deploy
1. Save the script as `StopAllEC2.py`.
2. Deploy it to an AWS Lambda function.
3. Schedule the Lambda function using a CloudWatch rule to run daily at specific time.

## IAM Role Requirements
The Lambda function requires an IAM role with the following permissions:
- `ec2:DescribeInstances`
- `ec2:StopInstances`

## Test Instructions
1. Add running EC2 instances in your AWS account.
2. Trigger the Lambda function manually or via the CloudWatch schedule.
3. Verify that all running EC2 instances are stopped.


