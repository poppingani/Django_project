"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from djangoapp2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('travel/',views.travel),
    path('travel2/',views.travel2),
    path('book/',views.book),
    path('travel3/',views.travel3),
    path('travel4/',views.travel4),
    path('travel5/',views.travel5),
    path('travel6/',views.travel6),
    path('confirm/',views.confirm)
]
