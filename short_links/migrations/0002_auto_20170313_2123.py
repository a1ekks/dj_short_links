# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short_links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlink',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date'),
        ),
    ]
