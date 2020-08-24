from django.db import models


class BaseModel(models.Model):
    """
    Abstract Model Initial
    """
    created_at = models.DateTimeField('Fecha Creación', auto_now_add=True)
    modified_at = models.DateTimeField('Fecha Modificación', auto_now=True)
    is_active = models.BooleanField('Activo', default=True)

    @classmethod
    def verbose_name(cls):
        return cls._meta.verbose_name

    class Meta:
        abstract = True
