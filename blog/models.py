# coding: utf-8
from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
    api_url = models.CharField(max_length=200)
    blog_url = models.CharField(max_length=200)
    pushed_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)