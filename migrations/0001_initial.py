# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('build', models.IntegerField(verbose_name='Build')),
                ('report', models.TextField(verbose_name='Report')),
                ('crdate', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('tstamp', models.DateTimeField(auto_now=True, verbose_name='Date changed')),
                ('is_solved', models.BooleanField(default=False, verbose_name='Is solved')),
                ('is_obsolete', models.BooleanField(default=False, verbose_name='Is obsolete')),
                ('application', models.ForeignKey(related_name=b'crashes', to='downloads.Application')),
            ],
            options={
                'ordering': ('-build', '-crdate', '-tstamp'),
                'verbose_name': 'Crash',
                'verbose_name_plural': 'Crashes',
            },
            bases=(models.Model,),
        ),
    ]
