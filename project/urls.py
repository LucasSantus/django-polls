from django.contrib import admin
from django.urls import path, include
from cadastro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('cadastro/', include('cadastro.urls')),
    path('administracao/', include('administracao.urls')),
]
