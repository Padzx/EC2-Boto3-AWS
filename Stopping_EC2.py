import json 
import boto3
from datetime import datetime


def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()

def Stop_Instances(instance_id):

    try:
        print("Stopping EC2 Instances")
        
        
        resource_ec2 = boto3.client("ec2")
        
        # Calling to stop the instance selected
        response = resource_ec2.stop_instances(InstanceIds=[instance_id])

        
        response_serializable = json.loads(json.dumps(response, default=serialize_datetime))

        print(json.dumps(response_serializable, indent=2))

        print("The Instance has been stopped")

    except Exception as e:
        print(e)
