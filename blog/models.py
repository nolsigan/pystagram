# coding: utf-8
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.conf import settings


class Blog(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    gh_url = models.CharField(max_length=200)
    blog_url = models.CharField(max_length=200)
    pushed_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # redirecting 할 url을 반환
    def get_absolute_url(self):
        return reverse_lazy('view_single_blog', kwargs={'blog_id': self.id})