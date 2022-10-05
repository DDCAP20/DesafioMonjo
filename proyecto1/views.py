from sys import flags
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Familiar

def registro(request):
    template = loader.get_template("template.html")
    datos = {
        "nombre01":"Andrea",
        "nombre02":"Sergio",
        "nombre03":"Josefina",
    }
    response=template.render(datos)
    return HttpResponse(response) 

def familia(request):
    familiares = Familiar.objects.all()
    if len(familiares) == 0:
        Familiar.objects.create(
        Nombre = "Andrea",
        Edad = 56,
        Nacimiento = "1966-7-21",
        )
        Familiar.objects.create(
        Nombre = "Sergio",
        Edad = 51,
        Nacimiento = "1971-3-12",
        )
        Familiar.objects.create(
        Nombre = "Josefina",
        Edad = 16,
        Nacimiento = "2006-7-4", 
        )
    template = loader.get_template("template02.html")
    datos = {
        "nombre01":familiares[0].Nombre,
        "nombre02":familiares[1].Nombre,
        "nombre03":familiares[2].Nombre,
        "edad01":familiares[0].Edad,
        "edad02":familiares[1].Edad,
        "edad03":familiares[2].Edad,
        "nacimiento01":familiares[0].Nacimiento,
        "nacimiento02":familiares[1].Nacimiento,
        "nacimiento03":familiares[2].Nacimiento,
    }
    response = template.render(datos)    
    return HttpResponse(response)




