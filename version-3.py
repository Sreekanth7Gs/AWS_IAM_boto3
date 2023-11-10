import boto3

def list_users_in_each_group():
    iam = boto3.client('iam')
    try:
        response = iam.list_groups()
        groups = response["Groups"]

        if not groups:
            print("No IAM groups found.")
            return

        for index, group in enumerate(groups, start=1):
            group_name = group['GroupName']
            print(f"{index}. Users in group: {group_name}")

            users_response = iam.get_group(GroupName=group_name)
            group_users = users_response["Users"]

            if group_users:
                for user in group_users:
                    print(f" - {user['UserName']}")
            else:
                print(f"No users in group {group_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

list_users_in_each_group()
