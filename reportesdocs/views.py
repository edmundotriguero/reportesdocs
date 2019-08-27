from django.http import HttpResponse

from datetime import datetime

# import para poder abrir un archivo

from io import open
import json


def reporte(request):

    request.POST['playlist']
    texto = {
        'status': 'ok 20000000'
    }

    return HttpResponse(json.dumps(texto), content_type='application/json')

def hi(request):
    
    
    # playlist = open('/home/edmundo/Documentos/proyectos/django/reportesdocs/playlist_02.03.04.m3u','r')
    # texto = playlist.readlines()
    

    with open("/home/edmundo/Documentos/proyectos/django/reportesdocs/playPollosCopa.m3u", "r") as fichero:
        texto = []
        for linea in fichero:

            if linea[-1] == '\n':
                linea = linea[:-1]

            texto.append(linea)

#     data = {
#             'status': 'ok',
#             'playlist': texto,

#     }
    
    # playlist.close()
    fichero.close()
    return HttpResponse(json.dumps(texto), content_type='application/json')