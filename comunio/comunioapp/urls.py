from django.conf.urls import include, url
from django.contrib import admin
from comunioapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'comunio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   
    
	 url(r'^$', views.home, name='home'),
]
