from django.conf.urls import url, include
from django.contrib import admin
from . import views



urlpatterns = [
    url(r'^$', views.success,name='success'),
    url(r'test/$', views.test,name='test'),
    url(r'cache/$', views.cache,name='cache'),
    url(r'api/$', views.api.as_view(),name='api'),

   ]
