"""pystagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from photo.views import single_photo, new_photo

urlpatterns = [
    # photos
    url(r'^photo/(?P<photo_id>\d+)$', single_photo, name='view_single_photo'),
    url(r'^photo/upload/$', new_photo, name='new_photo'),

    # login, out
    url(r'^accounts/login/', login, name='login',
        kwargs={
            'template_name': 'login.html'
        }
    ),
    url(r'^accounts/logout/', logout, name='logout'),

    # admin
    url(r'^admin/', admin.site.urls),

    # profiles
    url(r'^user/', include('profiles.urls')),

    # blog
    url(r'^blog/', include('blog.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)