from __future__ import absolute_import

from celery import shared_task
from celery.task import task

#@shared_task
@task(queue = 'priority_queue')
def test(param):
    return 'The test task executed with argument "%s" ' % param
