import boto3
import time

#Use AWS EC2 service
ec2 = boto3.resource('ec2')

#Set instance on which to perform operations by providing instance ID
instance = ec2.Instance('i-65bebc9d')

#Start the instance
instance.start()

#Wait for 10 seconds so that the newly started instance obtains an IP address
time.sleep(10)

#Print out its public IP address
print(instance.public_ip_address)
