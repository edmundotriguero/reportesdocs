from django.http import HttpResponse

from datetime import datetime

def hi(request):
    number = request.GET['numeros']
    return HttpResponse(str(number))