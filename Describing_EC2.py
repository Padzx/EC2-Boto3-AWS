import json
import boto3
from datetime import datetime 



def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()

def Describe_ec2_instance(instance_id):
    try:
        print(f"Describing EC2 Instance with ID: {instance_id}")
        
        
        resource_ec2 = boto3.client("ec2")
        
        
        # Call to describe the EC2 instance using the given ID
        response = resource_ec2.describe_instances(InstanceIds=[instance_id])

        
        response_serializable = json.loads(json.dumps(response, default=serialize_datetime))

        
        print(json.dumps(response_serializable, indent=2)) 

    except Exception as e:
        print(e)

# Calling the function to describe an EC2 instance using a specific ID
Describe_ec2_instance('your specific ID')
