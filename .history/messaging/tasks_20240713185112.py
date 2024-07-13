# myapp/tasks.py

from celery import shared_task
from django.core.mail import send_mail
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import traceback
import os
from datetime import datetime

@shared_task
def send_email(to_email):
  send_mail(
        'Test Email',
        'This is a test email.',
        'hi@demomailtrap.com',
        [to_email],
        fail_silently=False,
    )

def log_message():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Talktome request at {current_time}")
