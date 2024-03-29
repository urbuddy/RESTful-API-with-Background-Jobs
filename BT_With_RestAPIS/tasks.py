from time import sleep

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def test_func():
    for i in range(10):
        print(i)
    return "Done"


@shared_task
def send_email(sub, msg, to_user):
    subject = sub
    body = msg
    receiver = [to_user]
    sender = settings.EMAIL_HOST_USER
    send_mail(subject, body, sender, receiver)
    return "Email Sent"


@shared_task
def process_large_data(data):
    # Task to process large data sets
    # Your data processing logic here
    sleep(20)  # Simulate a long-running task
    print("Large data processed successfully")