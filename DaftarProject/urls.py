"""DaftarProject URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Daftar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.user_register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.userlogout, name='logout'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('create_post/<int:Profile_id>/', views.create_post, name='create_post'),
    path('search_user/', views.search_user, name='search_user'),
    path('follow/<int:Profile_id>/', views.follow_user, name="follow-button"),
    path('followers_page/<int:Profile_id>/', views.followers_page, name='followers_page'),
    path('following_page/<int:Profile_id>/', views.following_page, name='following_page'),
    path('user_profile/<int:Profile_id>/', views.user_profile, name='user_profile'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)