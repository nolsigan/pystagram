from __future__ import unicode_literals
from django import forms
from photo.models import Photo

class PhotoEditForm(forms.ModelForm):
	class Meta:
		model = Photo
		exclude = ('filtered_image_file', 'user')