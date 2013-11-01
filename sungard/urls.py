""" The URLS file.
"""
from django.conf.urls import patterns, include, url
from sungard.carsview import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^rest/sungard/cars$', CarApiListView.as_view() ),
    url(r'^rest/sungard/cars/(?P<id>\d+)$', CarApiUpdateView.as_view() ),
    # Examples:
    # url(r'^$', 'sungard.views.home', name='home'),
    # url(r'^sungard/', include('sungard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

