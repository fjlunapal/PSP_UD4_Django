from django.http import HttpResponse
import datetime

def saludo(request):

    documento="""<html>
    <body>
    <h1>
    Hola mundo
    </h1>
    </body>
    </html>"""

    return HttpResponse("HOLA MUNDO")

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
