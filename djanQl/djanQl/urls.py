"""
URL configuration for djanQl project.

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
from django.urls import path
from homepage.views import home_view
from homepage.views import context_view
from homepage.views import forloop_view
from student.views import student_details_view
from student.views import student_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view , name="home_view"),
    path('context/', context_view),
    path('forloop/', forloop_view),
    path('student/', student_details_view),
    path('create/', student_create_view)
]
