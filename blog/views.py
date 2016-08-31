# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog

# show single blog
def single_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    response_text = '<p>{blog_id}번 블로그입니당</p>'
    response_text += '<p>{api_url}</p>'
    response_text += '<p>{blog_url}</p>'
    response_text += '<p>{pushed_at}</p>'

    return HttpResponse(response_text.format(
        blog_id = blog_id,
        api_url = blog.api_url,
        blog_url = blog.blog_url,
        pushed_at = blog.pushed_at
        )
    )

def all_blogs(request):
    return render(request, 'index.html', {
        'blogs': Blog.objects.all
    })
