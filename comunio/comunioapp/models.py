from django.db import models

# Create your models here.

class Equipo(models.Model):
	numero = models.CharField(max_length=30)
	jugadores = models.TextField()
	fecha = models.DateTimeField()
