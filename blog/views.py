# coding: utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Blog
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import BlogNewForm
from .tasks import batch_send_email


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
    return render(request, 'index.html', {
        'blogs': Blog.objects.all,
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

    # blog = get_object_or_404(Blog, id=request.POST.get('id'))
    # blog.users.add(request.user)

    batch_send_email.delay()
    return JsonResponse({'status': 'ok'})
