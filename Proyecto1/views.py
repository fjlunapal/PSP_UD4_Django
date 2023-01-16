from django.http import HttpResponse
import datetime

from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre = nombre
        self.apellido = apellido


def saludo(request):

    p1=Persona("Javier", "De la flor")
    # nombre="Felix"
    # apellido="Reyes"
    temas_curso=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegues"]
    ahora=datetime.datetime.now()

    doc_externo=open("C:/Users/FJLun/Desktop/PROYECTO DJANGO/Proyecto1/Proyecto1/templates/template1.html")

    tmpl=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha_actual":ahora, "temas":temas_curso})

    documento=tmpl.render(ctx)

    return HttpResponse(documento)

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
