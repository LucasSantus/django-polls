from django.db import models
from autoslug import AutoSlugField

class BaseModel(models.Model):
    is_active = models.BooleanField(verbose_name = "Ativo", default = True)
    create_at = models.DateTimeField(verbose_name = "Data & Hora registrado", auto_now_add = True)
    update_at = models.DateTimeField(verbose_name = "Data & Hora modificado", blank = True, null = True, editable = True)
    desactivate_at = models.DateTimeField(verbose_name = "Data & Hora desativado", blank = True, null = True, editable = True)

    class Meta:
        abstract = True

class Base(BaseModel):
    title = models.CharField(verbose_name = "Título", max_length = 100, unique = True)
    slug = AutoSlugField(populate_from = 'title', unique_with = [ 'title' ], unique = True, editable = True)

    class Meta:
        abstract = True

"""

"""