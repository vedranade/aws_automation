import boto3

ec2 = boto3.resource('ec2')
for image in ec2.images.filter(Owners=['self']):
    ami = ec2.Image(image.id)
    print (ami.creation_date[0:10])
