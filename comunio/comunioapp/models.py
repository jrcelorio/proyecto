from django.db import models

# Create your models here.

class Equipo(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()

			def __str__(self):
					return '%s' % (self.nombre)

class Jugadores(models.Model):
	nombre = models.CharField(max_length=30)
	Equipo = models.TextField()
	equipos = models.ManyToManyField(Equipo, 
	through='equipo_jugador')
	edad = models.IntegerField()
	
			def __str__(self):
					return '%s' % (self.nombre)

class Jornada(models.Model):
	numero = models.TextField()
	puntuacion = models.TextField()

	def __str__(self):
		return '%s' % (self.nombre)

class equipo_jugador(models.Model):
	Equipo = models.ForeignKey(Equipo)
	Jugadores = models.ForeignKey(Jugadores)
	Jornada = models.IntegerField()

class jugador_jornada(models.Model):
	Jugadores = models.ForeignKey(Jugadores) 
	Jornada = models.ForeignKey(Jornada)
	Puntuación = models.IntegerField()

class Noticias(models.Model):
	Descripcion = models.TextField()

	def __str__(self):
		return '%s' % (self.nombre)


