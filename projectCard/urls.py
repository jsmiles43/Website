from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^projects$', views.project, name='project'),
    url(r'^contact$', views.contact, name='contact'),
]
