from django.db import models
from django.contrib.auth.models import User

from core import models as core_models


class Role(core_models.BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name


class Application(core_models.BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        default_related_name = ''
        verbose_name = 'Aplicación'
        verbose_name_plural = 'Aplicaciones'

    def __str__(self):
        return self.name


class Permission(core_models.BaseModel):
    user = models.ForeignKey(User,
                             verbose_name='Usuario',
                             on_delete=models.CASCADE)
    role = models.ForeignKey(Role,
                             verbose_name='Rol',
                             on_delete=models.CASCADE)

    application = models.ForeignKey(Application,
                             verbose_name='Aplicación',
                             on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role', 'application')
        default_related_name = 'permissions'
        verbose_name = 'Aplicación'
        verbose_name_plural = 'Aplicaciones'

    def __str__(self):
        return f'{str(self.user)} ({str(self.role)} - {str(self.application)}'
