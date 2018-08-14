"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from posts.views import *
from django.views.static import serve
from django.conf import settings
from accounts.views import register
from django.urls import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.conf.urls import url
from serv.views import list_all_the_bloody_services

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', posts_list, name="posts_list"),
    path('accounts/register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', posts_list, name="home"),

    path('accounts/password-reset/', password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    path('accounts/password-reset/done/', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    path('accounts/password-reset/complete/', password_reset_complete, name='password_reset_complete'),

    path('services/', list_all_the_bloody_services ,name='hairdoes'),


    path('post/<int:id>', post_detail, name="post_detail"),
    path('post/<int:id>/edit', edit_post, name="edit_post"),
    path('post/add', add_post, name="add_post"),
    path('search', search_posts, name='search_posts'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('post/<int:id>/like', like_post, name="like_post"),
    path('post/<int:id>/unlike', unlike_post, name="unlike_post"),

    
]
