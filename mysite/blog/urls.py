from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import archive

urlpatterns = patterns('',
    # Examples:
    url(r'^$', archive),
)