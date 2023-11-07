from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myself(request):
    return HttpResponse('<h1><marquee>Hi I am akhil</h1></marquee>')
