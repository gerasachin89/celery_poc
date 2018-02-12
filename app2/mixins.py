from django.shortcuts import render
from django.http import HttpResponse
from app2.models import *

from django.db import connections
from django.db.models.query import QuerySet

class QuerySetExplainMixin:
    def explain(self):
        cursor = connections[self.db].cursor()
        print(self.query)
        cursor.execute('explain %s' % str(self.query))
        return cursor.fetchall()

QuerySet.__bases__ += (QuerySetExplainMixin, )
