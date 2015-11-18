from django.db import models

# Create your models here.

class Equipo(models.Model):
	nombre = models.CharField(max_length=30)
	estadio = models.TextField()

	def __str__(self):
		return '%s' % (self.nombre)

class Jugadores(models.Model):
	nombre = models.CharField(max_length=30)
	equipo = models.TextField()
	equipos = models.ManyToManyField(Equipo, 
	through='Equipo_jugador')
	edad = models.IntegerField()
	
	def __str__(self):
		return '%s' % (self.nombre)

class Jornada(models.Model):
	numero = models.TextField()
	puntuacion = models.TextField()

	def __str__(self):
		return '%s' % (self.nombre)

class Equipo_jugador(models.Model):
	equipo = models.ForeignKey(Equipo)
	jugadores = models.ForeignKey(Jugadores)
	jornada = models.IntegerField()

class jugador_jornada(models.Model):
	jugadores = models.ForeignKey(Jugadores) 
	jornada = models.ForeignKey(Jornada)
	puntuación = models.IntegerField()

class Noticias(models.Model):
	descripcion = models.TextField()

	def __str__(self):
		return '%s' % (self.nombre)


