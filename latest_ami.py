import boto3
import datetime

#Setting latest AMI information to zero
latest_ami_id = 'asdfasdf'
latest_ami_date = '0000-00-00'
latest_ami_time = '00-00-00'

ec2 = boto3.resource('ec2')

#Following for loop considers only private AMIs
for image in ec2.images.filter(Owners=['self']):
    print (image.id, image.creation_date[0:10], image.creation_date[11:19])
    current_ami_id = image.id
    current_ami_date = image.creation_date[0:10]
    current_ami_time = image.creation_date[11:19]
    if current_ami_date > latest_ami_date:
        latest_ami_id = current_ami_id
        latest_ami_date = current_ami_date
        latest_ami_time = current_ami_time
    elif current_ami_date == latest_ami_date: #If AMIs are created on same day, then creation time needs to be considered
        if current_ami_time > latest_ami_time:
            latest_ami_id = current_ami_id
            latest_ami_date = current_ami_date
            latest_ami_time = current_ami_time
    
    
    

print ("\nLatest AMI ID is:", latest_ami_id, latest_ami_date, latest_ami_time)
