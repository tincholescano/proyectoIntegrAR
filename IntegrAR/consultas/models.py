from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Consulta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='consultas', null=True)  # Permite nulos temporalmente
    enlace = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Area(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class ConsultaEspecifica(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name='consultas', null=True)  # Permite nulos temporalmente
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='consultas', null=True)  # Permite nulos temporalmente
    enlace = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)  # Campo para el ID (número de seguimiento)
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=100, blank=True)  # Para usuarios no registrados
    apellido = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    nucleo_familiar = models.CharField(max_length=100, blank=True)  # No obligatorio
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, related_name='mensajes', null=True)  # Permite nulos temporalmente
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='mensajes', null=True)  # Permite nulos temporalmente
    respuesta = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titulo} (ID: {self.id})"
