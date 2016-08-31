from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<blog_id>\d+)$',
        views.single_blog,
        name='view_single_blog'),

    url(r'$',
        views.all_blogs,
        name='view_all_blogs'),
]