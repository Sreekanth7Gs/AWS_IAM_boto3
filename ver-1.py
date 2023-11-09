import boto3

iam = boto3.client('iam')
cloudtrail = boto3.client('cloudtrail')

# Get a list of IAM users
users = iam.list_users()

last_login_times = {}

for user in users['Users']:
    user_name = user['UserName']
    
    response = cloudtrail.lookup_events(LookupAttributes=[{'AttributeKey': 'EventName', 'AttributeValue': 'ConsoleLogin'}, {'AttributeKey': 'Username', 'AttributeValue': user_name}], MaxResults=1)
    
    events = response.get('Events', [])
    if events:
        last_login_time = events[0]['EventTime']
        last_login_times[user_name] = last_login_time
    else:
        last_login_times[user_name] = "N/A"
for user_name, last_login_time in last_login_times.items():
    print(f"User Name: {user_name}, Last Login Time: {last_login_time}")
