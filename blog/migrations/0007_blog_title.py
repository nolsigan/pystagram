# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_need_notifi'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]