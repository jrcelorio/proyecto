from django.shortcuts import render
from comunioapp.models import Equipo

# Create your views here.

def home(request):
   lista_equipos = Equipo.objects.all()
   return render(request, 'comunioapp/index.html', {'lista_equipos': lista_equipos })
