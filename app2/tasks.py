from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task import task

#@task(queue = 'feeds')
@shared_task
def add(x, y):
    return x + y


@shared_task
def mexitul(x, y):
    return x * y
