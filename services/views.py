from django.http import HttpResponse

def index(request):
    return HttpResponse("Servicios")



#TEST
from django.shortcuts import render

def test(request):
    return render(request, 'services.html',{})