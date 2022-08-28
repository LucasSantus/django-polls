from django.urls import path, include
from votations.views import create_room

urlpatterns = [
    path('rooms/', include([
        path("create/", create_room, name="create_room"),
        # path("change/<int:id_room>/", change_room, name="change_room"),
        # path("connect/", connect_room, name="connect_room"),
    ])),
]