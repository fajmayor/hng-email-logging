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

@shared_task(name='tasks.send_email')
def send_email(recipient):
    print(f"Attempting to send email to {recipient}")
    logging.info(f"Attempting to send email to {recipient}")
    try:
        smtp_server = 'live.smtp.mailtrap.io'
        port = 2525
        username = 'api'
        password = os.getenv('MAILTRAP_API_TOKEN', '12a6cdd24f44e3eb2f5417e8647c502d')

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Awesome HNG!"
        msg['From'] = "Mayowa Fajube <hi@demomailtrap.com>"
        msg['To'] = recipient

        text = "Newsletter sent successfully"
        html = """
        <!doctype html>
        <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        </head>
        <body>
            <p>Welcome to FAJMAYOR's Newsletter</p>
        </body>
        </html>
        """

        msg_page = MIMEText(text, 'plain')
        msg_email = MIMEText(html, 'html')

        msg.attach(msg_page)
        msg.attach(msg_email)

        logging.info(f"Connecting to SMTP server: {smtp_server}:{port}")
        with smtplib.SMTP(smtp_server, port, timeout=30) as server:
            logging.info("Starting TLS")
            server.starttls()
            logging.info("Logging in")
            server.login(username, password)
            logging.info("Sending email")
            server.sendmail(msg['From'], recipient, msg.as_string())

        print(f"{recipient} message se")
        logging.info(f"Email sent successfully to {recipient}")
    except (smtplib.SMTPException, IOError) as e:
        error_message = f"Failed to send email to {recipient}. Error: {str(e)}\n{traceback.format_exc()}"
        print(error_message)
        logging.error(error_message)
        raise send_email.retry(exc=e, countdown=60)  # Retry after 60 seconds
    except Exception as e:
        error_message = f"Unexpected error when sending email to {recipient}. Error: {str(e)}\n{traceback.format_exc()}"
        print(error_message)
        logging.error(error_message)
        raise

def log_message():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"Talktome request at {current_time}")
