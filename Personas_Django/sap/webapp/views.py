from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona

# Create your views here.

def bienvenido(request):
    # mensajes = {"msg1":"Valor mensaje 1","msg2":"Valor mensaje 2"}
    no_personas = Persona.objects.count() #Objects se utiliza para ejecutar comandos para entrar a la base de datos.

    personas = Persona.objects.all()

    return render(request,"bienvenido.html",{"no_personas":no_personas,"personas":personas})


# def despedirse(request):
#     return HttpResponse("Hasta luego")

# def contacto(request):
#     return HttpResponse("Nombre : Felipe Castro \nTelefono : 3172669966")
