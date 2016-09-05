# coding: utf-8
from __future__ import unicode_literals
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.conf import settings


class Blog(models.Model):
    class Meta:
        ordering = ['-created_at']

    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    gh_url = models.CharField(max_length=200)
    blog_url = models.CharField(max_length=200)
    pushed_at = models.DateTimeField(auto_now_add=True)
    need_notifi = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # redirecting 할 url을 반환
    def get_absolute_url(self):
        return reverse_lazy('view_single_blog', kwargs={'blog_id': self.id})


    # gh_url을 api url로 치환
    def get_api_url(self):
        url = self.gh_url
        pieces = url.split('/')
        if pieces[0] != 'https:':
            return False, '주소 프로토콜이 유효하지 않습니다.'
        elif pieces.__len__() != 5 or pieces[1] != '' or pieces[2] != 'github.com':
            return False, '주소가 유효하지 않습니다'

        api_url = pieces[0] + '//api.github.com/repos/' + pieces[3] + '/' + pieces[4]
        return True, api_url
