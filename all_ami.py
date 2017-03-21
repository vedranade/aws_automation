#This script displays only AMI IDs in current set region. Be sure to set credentials and region by running the 'aws configure' command

import boto3

ec2 = boto3.resource('ec2')
for image in ec2.images.filter(Owners=['self']):
        print (image.id)
