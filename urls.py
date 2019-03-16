# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import methods

urlpatterns = (
    url(r'^crashreport\/submit\.php$', methods.post_crashreport, name='post_crashreport'),
    url(r'^issues\.xml$', methods.post_issue, name='post_issue'),
)
