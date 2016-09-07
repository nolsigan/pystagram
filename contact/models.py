from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse_lazy


class Contact(models.Model):
    class Meta:
        ordering = ['-created_at']

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

