# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 06:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='api_url',
            new_name='gh_url',
        ),
    ]
