# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Crash

class CrashAdmin(admin.ModelAdmin):
    search_fields = ('report',)
    list_display = ('application', 'build',
                    'crdate', 'tstamp',
                    'is_solved', 'is_obsolete')
    list_filter = ('application', 'build',
                   'is_solved', 'is_obsolete',
                   'crdate', 'tstamp')
    date_hierarchy = 'crdate'

admin.site.register(Crash, CrashAdmin)
