from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    
class TareaEscolar(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()
    completada = models.BooleanField(default=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    