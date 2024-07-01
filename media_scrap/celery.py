import os 
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'media_scrap.settings')

celery = Celery('media_scrap')
celery.config_from_object('django.conf:settings', namespace='CELERY')
celery.autodiscover_tasks()