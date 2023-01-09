from django.http import HttpResponse
import datetime

from django.template import Template, Context

def saludo(request):

    doc_externo=open("C:/Users/FJLun/Desktop/PROYECTO DJANGO/Proyecto1/Proyecto1/templates/template1.html")

    tmpl=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

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
