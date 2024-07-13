# messaging_system/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messaging_system.settings')

app = Celery('messaging_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()