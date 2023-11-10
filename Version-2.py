import boto3

def list_attached_policies_to_users():
    iam = boto3.client('iam')
    try:
        response = iam.list_users()
        users = response["Users"]
        if not users:
            print("No IAM users found.")
            return
        for index, user in enumerate(response['Users'], start=1):
            user_name = user['UserName']
            print(f"{index}. Policies attached to user: {user_name}")

            attached_policies = iam.list_attached_user_policies(UserName=user_name)['AttachedPolicies']
            print(f"Checked attached policies for user: {user_name}")

            if attached_policies:
                print(f"Policies attached to user {user_name}:")
                for policy in attached_policies:
                    print(f"  - {policy['PolicyName']}")
            else:
                print(f"No policies attached to {user_name}")
    except Exception as e:
        print(f"An error occurred: {e}")

list_attached_policies_to_users()
