from django.conf.urls import patterns, url
from places import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^details/', views.details, name='details'),
        )
