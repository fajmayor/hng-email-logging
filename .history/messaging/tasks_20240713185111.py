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



def log_message():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Talktome request at {current_time}")
