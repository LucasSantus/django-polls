from django.urls import path, include
from votations.views import votations_room, create_votation

urlpatterns = [
    path('votations/', include([
        path("room/<slug:slug_room>/", votations_room, name="votations_room"),
        path("create/", create_votation, name="create_votation"),
        # path("change/<slug:slug_votation>/", change_votation, name="change_votation"),
        # path("desactivate/<slug:slug_votation>/", desactivate_votation, name="desactivate_votation"),
    ])),
]