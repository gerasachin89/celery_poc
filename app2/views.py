from django.shortcuts import render
from django.http import HttpResponse
from app2.models import *
from datetime import datetime, timedelta
from django.template import Context
from app2.mixins import QuerySetExplainMixin
from django.core.cache import cache
from rest_framework import generics
from app2.serializers import *
import redis
conn = redis.Redis('localhost')
# Create your views here.


def success(request):
    if request.GET.get('office'):
        print("$$$$$$$$", request.GET.get('office'))                               #if we passs query parameter ?office=foobar
    #print("EXPLAIN2",Person.objects.all().explain())                             # all query
    #print("EXPLAIN",Article.objects.filter(publications=1).explain())           # M2M
    #print("EXPLAIN",Person.objects.filter(first_name='"Sachin"').explain())     # filter against CharField
    #print("EXPLAIN",Person.objects.filter(pk=1).explain())                      # filter against int(pk)
    #print("EXPLAIN1",Person.objects.filter(id='1').explain())                   # filter against int(pk)
    #print("EXPLAIN", Person.objects.filter(office__id=1).explain())             # M2M Reverse

    #print("REDIS DICTIONARY",Person.objects.last().__dict__)
    redis_dict = Person.objects.last().__dict__
    a = conn.hmset("pythonDict", redis_dict)
    b = conn.hgetall("pythonDict")
    #print("_______________b________________",b)

    return HttpResponse(Person.objects.all().explain())

def test(request):
    #context['recipe'] = dict( image='http://localhost:8000/static/images/test1.jpg')
    image = Person.objects.get(pk=6)
    print(image)
    return render(request, "test.html", {'recipe': image})

def cache(request):
    #context['recipe'] = dict( image='http://localhost:8000/static/images/test1.jpg')
    image = Person.objects.get(pk=6)
    print(image)
    return render(request, "cache.html", {'recipe': image})


class api(generics.ListAPIView):
    serializer_class = upcellacceptSerializer
    queryset = Person.objects.all()





#((1L, u'SIMPLE', u'app2_person', None, u'ALL', None, None, None, None, 2L, 100.0, None),))

# [(0, u'Init', 0, 10, 0, u'', u'00', None),
# (1, u'OpenRead', 0, 37, 0, u'3', u'00', None),
# (2, u'Rewind', 0, 8, 0, u'', u'00', None),
# (3, u'Rowid', 0, 1, 0, u'', u'00', None),
# (4, u'Column', 0, 1, 2, u'', u'00', None),
# (5, u'Column', 0, 2, 3, u'', u'00', None),
# (6, u'ResultRow', 1, 3, 0, u'', u'00', None),
# (7, u'Next', 0, 3, 0, u'', u'01', None),
# (8, u'Close', 0, 0, 0, u'', u'00', None),
# (9, u'Halt', 0, 0, 0, u'', u'00', None),
# (10, u'Transaction', 0, 0, 54, u'0', u'01', None),
# (11, u'TableLock', 0, 37, 0, u'app2_person', u'00', None),
# (12, u'Goto', 0, 1, 0, u'', u'00', None)]

# tod = datetime.now()
# print("tod", tod.strftime('%Y-%m-%d %H:%M:%S.%f'))
# td = tod.strftime('%Y-%m-%d %H:%M')
# print("---string date---", "'"+str(tod)+"'")
#print("EXPLAIN1",Office.objects.filter(doj__lte=tod).explain())
#print(Office.objects.filter(doj__lte=tod).query)
#print("EXPLAIN1",Office.objects.filter(doj__year="'"+str(tod.year)+"'").explain())
#print("EXPLAIN",Person.objects.get(pk=1).explain())
