from django.contrib import admin
from comunioapp.models import Equipo
from comunioapp.models import Jugadores
from comunioapp.models import Jornada
from comunioapp.models import Noticias
from comunioapp.models import Equipo_jugador
# Register your models here.

admin.site.register(Equipo)
admin.site.register(Jugadores)
admin.site.register(Jornada)
admin.site.register(Noticias)
admin.site.register(Equipo_jugador)

