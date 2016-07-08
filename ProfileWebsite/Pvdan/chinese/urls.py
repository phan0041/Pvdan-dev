__author__ = 'Dan'


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^phrase$', views.phrase, name='phrase'),
    url(r'^sentence$', views.sentence, name='sentence'),
    url(r'^music$', views.music, name='music'),
]
