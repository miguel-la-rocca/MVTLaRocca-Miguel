from django.db import models

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)
    