from django.shortcuts import render
from blog.models import Configuracion

def index(request):
    configuracion = Configuracion.objects.first()
    return render(request, 'blog/index.html', {'configuracion': configuracion} )
