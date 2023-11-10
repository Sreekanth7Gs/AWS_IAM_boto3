import boto3

iam = boto3.client('iam')
cloudtrail = boto3.client('cloudtrail')

users = iam.list_users()['Users']

last_login_times = {}

for user in users:
    user_name = user['UserName']
    
    response = cloudtrail.lookup_events(
        LookupAttributes=[
            {'AttributeKey': 'EventName', 'AttributeValue': 'ConsoleLogin'},
            {'AttributeKey': 'Username', 'AttributeValue': user_name}
        ],
        MaxResults=1
    )
 
    if response.get('Events'):
       last_login_times[user_name] = response['Events'][0]['EventTime']
    else:
       last_login_times[user_name] = "N/A"


for user_name, last_login_time in last_login_times.items():
    print("\n")
    print(f"User Name: {user_name}, Last Login Time: {last_login_time}")
    print('\n')
