from django.conf.urls import url
from comunioapp import views

urlpatterns = [
   url(r'^$', views.home, name='home'),
	url(r'^(?P<alineacion_id>\d+)/$', views.detalle_alineacion, name='detalle_alineacion'),
	 url(r'^registro$', views.registro, name='registro'),
    url(r'^login$', views.loginpage, name='login'),
    url(r'^logout$', views.logoutpage, name='logout'),	
]
