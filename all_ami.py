import boto3

ec2 = boto3.resource('ec2')
for image in ec2.images.filter(Owners=['self']):
        print (image.id)
