from __future__ import unicode_literals
from django import forms
from blog.models import Blog

class BlogNewForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('api_url', 'blog_url')