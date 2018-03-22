from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task import task
import time
from django.conf import settings
from celery import Celery
from cel_poc.celery import app
# app = Celery('testsessionstasks', backend='redis://localhost:6379/1?new_join=1',
#                 broker='redis://localhost:6379/2')

#@task(queue = 'feeds')
@shared_task
def add(x, y):
    time.sleep(30)
    return x + y


@task(acks_late=True, reject_on_worker_lost=True)
def mul(x, y):
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


@app.task(name="app2.subtract", acks_late=True)
def sub(x, y):
    time.sleep(30)
    return x - y


@app.task(name="app2.divide", acks_late=True)
def div(x, y):
    time.sleep(30)
    return x / y
