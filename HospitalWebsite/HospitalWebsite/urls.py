"""
URL configuration for HospitalWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from userApp import views

urlpatterns = [
    path('admin/', include('adminApp.admin_urls')),
    path('',views.home),
    path('user/about/',views.about),
    path('user/award/',views.award),
    path('user/teams/',views.teams),
    path('user/departments/',views.departments),
    path('user/blog/',views.blog),
    path('user/contact/',views.contact),
    path('user/appoinment/',views.appoinment),
    path('user/social_media/',views.social_media),
    path('user/gallery/',views.gallery),
    path('user/testimonial/',views.testimonial),
    path('user/privacy_policy/',views.privacy_policy),
    path('user/inauguration/',views.inauguration)






]
