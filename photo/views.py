# coding: utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Photo
from photo.forms import PhotoEditForm


# show single photo
def single_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)

    response_text = '<p>{photo_id}번...{photo_id}번 사진을 보여 드릴게요.</p>'
    response_text += '<p>{photo_url}</p>'
    response_text += '<p><img src="{photo_url}" /></p>'

    return HttpResponse(response_text.format(
        photo_id=photo_id,
        photo_url=photo.image_file.url
        )
    )


# create new photo
@login_required
def new_photo(request):
    if request.method == "GET":
        edit_form = PhotoEditForm()
    elif request.method == "POST":
        edit_form = PhotoEditForm(request.POST, request.FILES)

        if edit_form.is_valid():
            new_photo = edit_form.save(commit=False)
            new_photo.user = request.user
            new_photo.save()
            return redirect(new_photo.get_absolute_url())

    return render(
        request,
        'new_photo.html',
        {
            'form': edit_form,
        }
    )