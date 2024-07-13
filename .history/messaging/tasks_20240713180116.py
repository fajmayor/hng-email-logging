# messaging/tasks.py
from celery import shared_task
from django.core.mail import send_mail
import logging
from datetime import datetime

@shared_task
def send_email(to_email):
  send_mail(
        'Test Email',
        'This is a test email.',
        'guest04real@',
        [to_email],
        fail_silently=False,
    )

  #with smtplib.SMTP('smtp.example.com') as server:
      #server.login('your_email@example.com', 'your_password')
      #server.sendmail('your_email@example.com', [to_email], msg.as_string())

@shared_task
def log_message():
    logging.basicConfig(filename='/var/log/messaging_system.log', level=logging.INFO)
    logging.info(f'Talktome endpoint hit at {datetime.now()}')

#   current_time = now().strftime('%Y-%m-%d %H:%M:%S')
#   logger.info(f"Talk to me request received at {current_time}")