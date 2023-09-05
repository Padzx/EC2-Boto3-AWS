import boto3
import json
from datetime import datetime 

def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()


def Reboot_Instance(instance_id):

    try:
        print("Rebooting EC2 Instance")
        
        
        resource_ec2 = boto3.client("ec2")
        
        # Calling to restart the instance selected
        response = resource_ec2.reboot_instances(InstanceIds=[instance_id])

        
        response_serializable = json.loads(json.dumps(response, default=serialize_datetime))

        print(json.dumps(response_serializable, indent=2))

    except Exception as e:
        print(e)
