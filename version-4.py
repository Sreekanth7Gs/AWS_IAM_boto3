import boto3
from datetime import datetime, timedelta
from botocore.exceptions import ClientError

def get_inactive_users():
    users = [
        {"email": "manojkumar052023@gmail.com", "last_login": datetime.now() - timedelta(days=1)},
        {"email": "gssreekanth21@gmail.com", "last_login": datetime.now() - timedelta(days=3)},
        {"email": "manoj11223s@gmail.com", "last_login": datetime.now() - timedelta(days=1)},  
    ]

    inactive_users = [user for user in users if (datetime.now() - user["last_login"]).days > 2]

    return inactive_users

def send_notification_email(user_email):
    ses = boto3.client('ses')

    sender_email = 'gssreekanth016@gmail.com'
    subject = 'Inactive User Notification'
    message = 'You have not been active for the last 2 days. Please log in to your account.'

    try:
        response = ses.send_email(
            Destination={
                'ToAddresses': [user_email],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': message,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': subject,
                },
            },
            Source=sender_email,
        )
        print(f"Email sent to {user_email}: Message ID {response['MessageId']}")
    except ClientError as e:
        print(f"Error sending email to {user_email}: {e.response['Error']['Message']}")

def main():
    inactive_users = get_inactive_users()

    for user in inactive_users:
        user_email = user["email"]
        send_notification_email(user_email)

if __name__ == "__main__":
    main()
