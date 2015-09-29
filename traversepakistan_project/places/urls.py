from django.conf.urls import patterns, url
from places import views

urlpatterns = patterns('',
                       url(r'^browse/(?P<region>\w*)/(?P<category>\w*)', views.browse, name='browse'),
                       url(r'^details/(?P<name>\w+)', views.details, name='details'),
                       url(r'^$', views.index, name='index'),
                       url(r'^api/', views.api, name='api'),
                       url(r'^weather/', views.weather, name='api'),
                       )
