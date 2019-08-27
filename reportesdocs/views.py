from django.http import HttpResponse

from datetime import datetime

# import para poder abrir un archivo

from io import open
import json

def hi(request):
    
    
    # playlist = open('/home/edmundo/Documentos/proyectos/django/reportesdocs/playlist_02.03.04.m3u','r')
    # texto = playlist.readlines()
    

    with open("/home/edmundo/Documentos/proyectos/django/reportesdocs/playlist_02.03.04.m3u", "r") as fichero:
        texto = []
        for linea in fichero:
            texto.append(linea)

    # playlist.close()
    fichero.close()
    return HttpResponse(json.dumps(texto), content_type='application/json')