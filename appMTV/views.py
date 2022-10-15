from django.shortcuts import render
from appMTV.models import Familiar

# Create yodef index(request):
def index(request):
    return render(request, "appMTV/saludar.html")

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "appMTV/familiares.html", {"lista_familiares": lista_familiares})

