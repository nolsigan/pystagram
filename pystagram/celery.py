from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pystagram.settings')

from django.conf import settings  # noqa

app = Celery('crawler', broker='redis://localhost:6379/0')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.conf.update(
    CELERYBEAT_SCHEDULE={
        'check-push-at-2-am': {
            'task': 'blog.tasks.crawl_blogs',
            'schedule': crontab(minute=0, hour=17)
        },
        'send-notification-email-at-10-am': {
            'task': 'blog.tasks.batch_send_email',
            'schedule': crontab(minute=0, hour=1)
        }
    },
)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))