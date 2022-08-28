from django.db import models

class UserRooms(models.Model):
    room = models.ForeignKey("votations.Room", on_delete = models.CASCADE, verbose_name = "Sala de Votação", related_name = "room_UserRooms_FK")
    users = models.ManyToManyField("users.User", verbose_name = "Usuários", blank = True)
    is_active = models.BooleanField(default = True)
    create_at = models.DateTimeField(verbose_name = "Data da Criação", auto_now_add = True)
    update_at = models.DateTimeField(verbose_name = "Data da Atualização", auto_now = False)
    desactive_at = models.DateTimeField(verbose_name = "Data da Desativação", auto_now = False)

    class Meta:
        verbose_name = "Sala de Usuário"
        verbose_name_plural = "Sala de Usuários"
        db_table = "user_rooms"
        app_label = "links"

    def __str__(self):
        return self.room
