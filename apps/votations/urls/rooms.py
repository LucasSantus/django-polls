from django.urls import path, include
# from votations.views import create_room, change_room, desactivate_room, connect_room
from votations.views import *

urlpatterns = [
    path('rooms/', include([
        path("create/", create_room, name="create_room"),
        path("change/<slug:slug_room>/", change_room, name="change_room"),
        path("desactivate/<slug:slug_room>/", desactivate_room, name="desactivate_room"),
        path("connect/", connect_room, name="connect_room"),

        path("room/<slug:slug_room>/", votations_room, name="votations_room"),
        path("create/", create_votation, name="create_votation"),
    ])),

    # path('votations/', include([
    #     path("room/<slug:slug_room>/", votations_room, name="votations_room"),
    #     path("create/", create_votation, name="create_votation"),
    #     # path("change/<slug:slug_votation>/", change_votation, name="change_votation"),
    #     # path("desactivate/<slug:slug_votation>/", desactivate_votation, name="desactivate_votation"),
    # ])),
]