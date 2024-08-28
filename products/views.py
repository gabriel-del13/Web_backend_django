from django.http import HttpResponse


def products(request):
    return HttpResponse("Products")

def products_id(request,id):
    if id == 1:
        return HttpResponse("Hola")



#TEST
from django.shortcuts import render

def test(request):
    return render(request, 'index.html',{})