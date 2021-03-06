# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-13 04:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sosapp', '0010_auto_20170213_0922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iexperiencemodel',
            options={'ordering': ('-i_created',)},
        ),
        migrations.AlterModelOptions(
            name='reportoncemodel',
            options={'ordering': ('-r_created',)},
        ),
        migrations.AddField(
            model_name='iexperiencemodel',
            name='i_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reportoncemodel',
            name='r_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
