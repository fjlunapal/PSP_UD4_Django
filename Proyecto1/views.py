from django.http import HttpResponse
import datetime

from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre = nombre
        self.apellido = apellido


def saludo(request):

    p1=Persona("Javier", "Flor")
    # nombre="Felix"
    # apellido="Reyes"
    temas_curso=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegues"]
    ahora=datetime.datetime.now()

    #doc_externo=open("C:/Users/FJLun/Desktop/PROYECTO DJANGO/Proyecto1/Proyecto1/templates/template1.html")

    #tmpl=Template(doc_externo.read())

    #doc_externo.close()

    #doc_externo=get_template('template1.html')

    #ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_actual":ahora, "temas":temas_curso})

    #documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_actual":ahora, "temas":temas_curso})

    return render(request, "template1.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_actual":ahora, "temas":temas_curso})

def cursoDjango(request):
    fecha_actual=datetime.datetime.now()

    return render(request, "psp1.html", {"dameFecha":fecha_actual})

def cursoCss(request):
    fecha_actual=datetime.datetime.now()

    return render(request, "css1.html", {"dameFecha":fecha_actual})
    
def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, agno):

    edadActual=21
    periodo=agno-2023
    edadFutura=edadActual+periodo
    documento="""<html>
    <body>
    <h1>
    En el año %s tendras %s años
    </h1>
    </body>
    </html>""" %(agno, edadFutura)

    return HttpResponse(documento)
    
