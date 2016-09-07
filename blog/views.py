# coding: utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Blog
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import BlogNewForm


# show single blog
def single_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    response_text = '<p>{blog_id}번 블로그입니당</p>'
    response_text += '<p>{gh_url}</p>'
    response_text += '<p>{blog_url}</p>'
    response_text += '<p>{pushed_at}</p>'

    return HttpResponse(response_text.format(
        blog_id=blog_id,
        gh_url=blog.gh_url,
        blog_url=blog.blog_url,
        pushed_at=blog.pushed_at
        )
    )


# show all blogs
def all_blogs(request):
    first = []
    second = []
    third = []
    i = 0

    blogs = list(Blog.objects.all())
    for blog in blogs:
        if i % 3 == 0:
            first.append(blog)
        elif i % 3 == 1:
            second.append(blog)
        else:
            third.append(blog)
        i += 1

    return render(request, 'index.html', {
        'col_1': first,
        'col_2': second,
        'col_3': third,
    })


# create a new blog
@user_passes_test(lambda u: u.is_superuser)
def new_blog(request):
    if request.method == 'GET':
        new_form = BlogNewForm()
    elif request.method == 'POST':
        new_form = BlogNewForm(request.POST, request.FILES)

        if new_form.is_valid():
            new_blog = new_form.save()
            return redirect(new_blog.get_absolute_url())

    return render(request, 'new.html', {
        'form': new_form,
    })


# subscribe
@login_required
def subscribe(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'wrong access'})

    blog = get_object_or_404(Blog, id=request.POST.get('id'))
    if request.user in blog.users.all():
        blog.users.remove(request.user)
    else:
        blog.users.add(request.user)

    return JsonResponse({'status': 'ok'})
