from django.contrib import admin
from comunioapp.models import Equipo
from comunioapp.models import Jugadores 
from comunioapp.models import Noticias
from comunioapp.models import Jornada

admin.site.register(Equipo)
admin.site.register(Jugadores)
admin.site.register(Noticias)
admin.site.register(Jornada)
# Register your models here.
