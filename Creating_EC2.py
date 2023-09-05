import json
from datetime import datetime
import boto3


# Creating the Elastic Compute Cloud (EC2)

def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()

def Create_ec2_instance():
    try:
        print("Creating the Instance EC2")
        
        resource_ec2 = boto3.client("ec2")
        response = resource_ec2.run_instances(
            ImageId='ami-0f409bae3775dc8e5',
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName="YOU-KEY-PAIR",
            InstanceInitiatedShutdownBehavior='terminate',  
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': 'YOUR-NAME-INSTANCE'
                        },
                        # You can add more tags here, if need 
                    ]
                }
            ]
        )
        
        response_serializable = json.loads(json.dumps(response, default=serialize_datetime))
        
        print(json.dumps(response_serializable, indent=2))  
        
    except Exception as e:
        print(e)

    print("Instance EC2 Was Created!")

Create_ec2_instance()
