
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from celery import Celery
from cel_poc.celery import app


class Command(BaseCommand):
    args = '<arg arg ...>'
    app = Celery('cel_poc', backend='redis://localhost:6379/1?new_join=1',
                     broker='redis://localhost:6379/2')

    def handle(self, *args, **options):
        self.monitor_events(self.app)

    def monitor_events(self, app):
        state = app.events.State()
        def on_event(event):
            state.event(event)
            worker_dict = {}
            for worker in state.workers:
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                worker_dict[worker] = {}
                worker_dict[worker]["subtract"] = 0
                worker_dict[worker]["divide"] = 0
                for tup in state.tasks_by_worker(worker):
                    print("#######################")
                    print tup[1].as_dict()
                    if tup[1].as_dict()["state"] != "SUCCESS" and \
                                    tup[1].as_dict()["state"] != "PENDING":
                        if tup[1].as_dict()[
                            "name"] == "app2.subtract":
                            worker_dict[worker]["subtract"] += 1
                        if tup[1].as_dict()[
                            "name"] == \
                                "app2.divide":
                            worker_dict[worker]["divide"] += 1
            print "+++++++++++++++++++++++++++++++++++++++++++++++++++++"
            for key in worker_dict:
                print "######################"
                print "WORKER %s" % key
                print "#####################"
                print "===== PROCESSING ==="
                print "subtract task count: %d" % worker_dict[key][
                    "subtract"]
                print "div task count: %d" % worker_dict[key][
                    "divide"]


        with app.connection() as connection:
            recv = app.events.Receiver(connection, handlers={'*': on_event})
            recv.capture(limit=None, timeout=None, wakeup=True)
