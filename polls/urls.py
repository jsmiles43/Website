from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^expo$', views.expo, name='expo'),
    url(r'^time$', views.current_datetime, name = 'current_datetime'),


    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^expound/(?P<expounding>[0-9]+)/$', views.expound, name='expound')

]