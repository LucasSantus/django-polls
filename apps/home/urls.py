from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # INDEX
    path("", index, name="index"),
]