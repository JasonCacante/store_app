from django.db import models

# first import data models in this case User
from django.contrib.auth.models import User

# second import cascade from constraints
from django.db.models.deletion import CASCADE

# thrid import update module
from django.dispatch import receiver

# fourth import rewrite module
from django.db.models.signals import post_save

# fifth import types
from core.types.generos import Generos
from core.types.tipoid import TiposIdenficacion

# sixth global function to save profile image
def subir_avatar(instance, nombre_archivo):
    anterior_instacia = PerfilUsuario.objects.get(pk=instance.pk)
    anterior_instacia.img_perfil.delete()
    return "perfiles/" + nombre_archivo


# seventh we build our models
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, verbose_name="Usuario", on_delete=CASCADE)
    img_perfil = models.ImageField(
        verbose_name="Imagen-Perfil", upload_to=subir_avatar, null=True, blank=True
    )
    genero_user = models.CharField(
        verbose_name="Género",
        choices=Generos,
        max_length=20,
        null=False,
        default="Otro",
    )
    tipo_identificacion = models.CharField(
        verbose_name="Tipo de Documento de Identidad",
        choices=TiposIdenficacion,
        max_length=50,
        null=False,
        default="Sin Identificar",
    )
    identificacion_usuario = models.CharField(
        verbose_name="Número de Identificación", max_length=50, null=False
    )
    direccion = models.TextField(verbose_name="Dirección Postal", null=True, blank=True)
    telefono = models.CharField(
        verbose_name="Télefono", max_length=20, null=True, blank=True
    )
    # Atributos de Auditoría
    create_at = models.DateField(
        auto_now=False,
        auto_now_add=True,
        verbose_name="Fecha De Creación",
        null=True,
        blank=True,
    )
    modify_at = models.DateField(
        auto_now=True,
        auto_now_add=False,
        verbose_name="Fecha de Actualización",
        null=False,
        blank=True,
    )
    # Metadata
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"
        ordering = ["usuario__username"]


# Function decorator for users
@receiver(post_save, sender=User)
def ensure_profile_exist(sender, instance, **kwards):
    if kwards.get("created", False):
        PerfilUsuario.objects.get_or_create(usuario=instance)
