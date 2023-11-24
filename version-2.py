import boto3

def list_user_policies(iam_client, username):
    try:
        response = iam_client.list_attached_user_policies(UserName=username)
        return response.get('AttachedPolicies', [])
    except Exception as e:
        print(f"Error listing policies for user {username}: {e}")
        return []

def main():
    iam_client = boto3.client('iam')

    try:
       
        response = iam_client.list_users()
        users = response.get('Users', [])

        if not users:
            print("No IAM users found.")
            return

        for user in users:
            username = user['UserName']
            user_policies = list_user_policies(iam_client, username)

            if user_policies:
                print(f"Policies attached to {username}:")
                for policy in user_policies:
                    print(f"  - {policy['PolicyName']} (ARN: {policy['PolicyArn']})")
            else:
                print(f"No policies attached to {username}")

            print("=" * 30)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
