from django.urls import path, include
from votations.views import create_room, change_room, desactivate_room

urlpatterns = [
    path('rooms/', include([
        path("create/", create_room, name="create_room"),
        path("change/<slug:slug_room>/", change_room, name="change_room"),
        path("desactivate/<int:id_room>/", desactivate_room, name="desactivate_room"),
        # path("connect/", connect_room, name="connect_room"),
    ])),
]