from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task import task
import time

#@task(queue = 'feeds')
@shared_task
def add(x, y):
    time.sleep(30)
    return x + y


@task(acks_late=True, reject_on_worker_lost=True)
def mexitul(x, y):
    time.sleep(30)
    return x * y

@task(bind=True, acks_late=True)
def add1(self, x, y):
    try:
        return x * y *z
    except Exception as e:
        self.update_state(state='FAILURE', meta={'exc': e})
        self.retry(countdown=2, exc=e)
        #self.retry(args=[5, 7], exc=e, countdown=30)
    return x + y
