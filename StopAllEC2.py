import boto3
import json

def lambda_handler(event, context):
    # Connect to the EC2 resource
    ec2_connection = boto3.resource(service_name="ec2", region_name="us-east-1")
    
    # Filter to get all running EC2 instances
    filter_ec2 = {"Name": "instance-state-name", "Values": ["running"]}
    
    # Iterate through all running instances and stop them
    for each in ec2_connection.instances.filter(Filters=[filter_ec2]):
        print(f"Stopping instance: {each.id}")
        each.stop()
    
    return {
        "statusCode": 200,
        "body": json.dumps("All running EC2 instances stopped.")
    }
