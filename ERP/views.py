from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def indexPage(request):
    return HttpResponse("This is the ERP Application Called")