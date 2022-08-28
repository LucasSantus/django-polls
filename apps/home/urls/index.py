from django.urls import path
from home.views import *

urlpatterns = [
    path('', index, name='index'),

    # CONTATO
    # path("contact/", contato, name="contato"),
]

handler404 = "home.views.error_404"