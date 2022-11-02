"""PrimerMTV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from appMTV.views import (index,  monstrar_familiares, 
                        BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, 
                        )
#from blog.views import index as blog_index



urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('mi-familia/', monstrar_familiares), 
  
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
     # EL paramatro pk hace referencia al identificador único en la base de datos para Familiar.
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('panel-familia/', include('panel_familia.urls')),
    path('blog/', include('blog.urls')),
]
