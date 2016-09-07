# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model


def profile(request, username):
    users = get_user_model()
    user = get_object_or_404(users, username=username)
    uid = -1
    if user.email != '' or user.first_name != '':
        uid = user.social_auth.get(provider='github').uid

    return render(request, 'profile.html', {
        'current_user': user,
        'uid': uid,
        'subscribes': user.blog_set.all().count,
    })
