import boto3

ec2 = boto3.client('ec2')

response = ec2.stop_instances(InstanceIds=['i-65bebc9d'])

print(response)
