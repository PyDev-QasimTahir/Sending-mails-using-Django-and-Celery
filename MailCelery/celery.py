from __future__ import unicode_literals, absolute_import
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MailCelery.settings')

app = Celery('MailCelery')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
