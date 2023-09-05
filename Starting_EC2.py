import json
import boto3
from datetime import datetime

def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    
def Start_Instances(instance_id):

    try:
        print("Starting EC2 Instances")
        
    
        resource_ec2 = boto3.client("ec2")
        
        # Calling to start the instance selected
        response = resource_ec2.start_instances(InstanceIds=[instance_id])

        
        response_serializable = json.loads(json.dumps(response, default=serialize_datetime))

        
        print(json.dumps(response_serializable, indent=2))

        print("The Instance has been started")

    except Exception as e:
        
        print(e)

