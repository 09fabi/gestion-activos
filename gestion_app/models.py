from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.db import models

class Activo(models.Model):
    titulo = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.titulo
    
class Report(models.Model):
    nombre_responsable = models.CharField(max_length=255)
    email = models.EmailField()
    estado_activo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    activo_titulo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre_responsable

class CustomUserManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError('El campo "correo" es obligatorio.')
        
        user = self.model(correo=self.normalize_email(correo), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(correo, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    correo = models.EmailField(unique=True)
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    nivel = models.CharField(max_length=15, default='usuario')
    genero = models.CharField(max_length=1, default='O')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='customuser_set')

    objects = CustomUserManager()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.correo