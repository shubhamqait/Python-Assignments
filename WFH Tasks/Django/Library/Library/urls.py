"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.models import User, Group
from django.contrib.admin.models import LogEntry
from LibraryManagementTool.admin import user_site

user_site.register(User)
user_site.register(Group)
admin.site.site_header = 'Library Management Portal'
admin.site.site_title = "Library"
admin.site.index_title = "Library"
user_site.site_header = 'Library Management Portal'
user_site.site_title = "Library"
user_site.index_title = "Library"
LogEntry.objects.all().delete()
admin.site.unregister(User)
admin.site.unregister(Group)

urlpatterns = [
    path('', admin.site.urls),
    path('myuser',user_site.urls),
]