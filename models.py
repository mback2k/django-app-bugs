# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from ..downloads.models import Application

class Crash(models.Model):
    application = models.ForeignKey(Application, related_name='crashes')
    build = models.IntegerField(_('Build'))
    report = models.TextField(_('Report'))

    crdate = models.DateTimeField(_('Date created'), auto_now_add=True)
    tstamp = models.DateTimeField(_('Date changed'), auto_now=True)

    is_solved = models.BooleanField(_('Is solved'), blank=True, default=False)
    is_obsolete = models.BooleanField(_('Is obsolete'), blank=True, default=False)

    class Meta:
        verbose_name = _('Crash')
        verbose_name_plural = _('Crashes')
        ordering = ('-build', '-crdate', '-tstamp')

    def __str__(self):
        return '%s Build %d' % (self.application, self.build)

"""
SQL-Statement to convert crash reports saved as Redmine issues:

SELECT
 1 AS application_id,
 CONVERT(REPLACE(`subject`, 'Crash Report Build ', ''), INTEGER) AS build,
 `description` AS report,
 `created_on` AS crdate,
 `updated_on` AS tstamp,
 IF(`status_id`=3 OR `status_id`=5, 1, 0) AS is_solved,
 IF(`status_id`=4 OR `status_id`=6, 1, 0) AS is_obsolete
FROM `redmine`.`issues`
WHERE `subject` LIKE 'Crash Report Build %'
"""
