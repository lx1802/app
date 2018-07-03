from django.conf.urls import url
from myapp import views
from django.contrib import admin

urlpatterns = [
    url('', views.index),
]