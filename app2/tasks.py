from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task import task

#@task(queue = 'feeds')
@shared_task
def add(x, y):
    import time
    time.sleep(150)
    return x + y

#@task(queue = 'feeds')
@shared_task
def mexitul(x, y):
    import time
    time.sleep(100)
    return x * y


@task(bind=True)
def add1(self, x, y):
    try:
        return x * y *z
    except Exception as e:
        self.update_state(state='FAILURE', meta={'exc': e})
        self.retry(countdown=2, exc=e)
    return x + y
