from django.db import models
from home.models import BaseModel

class UserRooms(BaseModel):
    room = models.ForeignKey("votations.Room", on_delete = models.CASCADE, verbose_name = "Sala de Votação", related_name = "room_UserRooms_FK")
    users = models.ManyToManyField("users.User", verbose_name = "Usuários da Sala", blank = True)

    class Meta:
        verbose_name = "Sala de Usuário"
        verbose_name_plural = "Sala de Usuários"
        db_table = "user_rooms"
        app_label = "links"

    def __str__(self):
        return self.room.title
