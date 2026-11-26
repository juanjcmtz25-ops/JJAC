from django.shortcuts import render

def inicio (request):
    return render (request, "cortes/inicio.html")
def registro(request):
    return render (request, "cortes/formregistro.html")
def futbol(request):
    return render (request, "cortes/futbol.html")
