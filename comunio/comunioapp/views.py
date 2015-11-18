from django.shortcuts import get_object_or_404,render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from comunioapp.models import Equipo
from comunioapp.forms import ComunioForm

# Create your views here.

def home(request):
   lista_equipos = Equipo.objects.all()
   return render(request, 'comunioapp/index.html', {'lista_equipos': lista_equipos })

def detalle_alineacion(request,alineacion_id):
	receta = get_object_or_404(Alineacion, pk = alineacion_id)
	return render(request, 'comunioapp/detalle_alineacion.html', {'alineacion': alineacion })

def registro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()
	return render(request, "comunioapp/registro.html", {
'form': form,})

def loginpage(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect("/")
	else:
		form = AuthenticationForm()
	return render(request,'comunioapp/login.html', {'form': form,})  

def logoutpage(request):
	logout(request)
	return HttpResponseRedirect("/")

def addalineacion(request):
	if request.method == "POST":
		form = RecetaForm(request.POST)
		if form.is_valid():
			receta = form.save()
			receta.save()
			return HttpResponseRedirect("/")
	
