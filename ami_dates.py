#This simple script displays all AWS AMI creation dates in the current region. Current region is set in the AWS config file. Be sure to set credentials by running the 'aws configure' command


import boto3

ec2 = boto3.resource('ec2')
for image in ec2.images.filter(Owners=['self']):
    ami = ec2.Image(image.id)
    print (ami.creation_date[0:10])
