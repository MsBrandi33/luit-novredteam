import boto3

instances = ['i-0aa8275605821fff2, i-08b9127f6a0916183, i-0ca76a52468fb0211']
region = 'us-east-1'
ec2 = boto3.client('ec2', region_name=region)

    
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('instances stopped: ' + str(instances))
