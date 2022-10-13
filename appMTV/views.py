from django.shortcuts import render

# Create yodef index(request):
def index(request):
    return render(request, "appMTV/saludar.html")
