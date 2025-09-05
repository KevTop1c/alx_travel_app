"""
Celery configuration for alx_travel_app project
"""
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery('alx_travel_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    """Debug task for testing Celery configuration"""
    print(f'Request: {self.request!r}')