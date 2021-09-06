from django.contrib import admin
from django.urls import path, include, re_path
from . import settings_local
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Include URL APP's
    path('', include('home.urls')),
    path('usuario/', include('usuarios.urls')),
    path('', include('votacao.urls')),

    #Config URL's
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings_local.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] 