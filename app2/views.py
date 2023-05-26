from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhiraj(request):
    return HttpResponse('searching for monalisa')
def aakash(request):
    return HttpResponse('searching for job')
def dr_amma(request):
    return HttpResponse('<h1><marquee>hello dr garu ,sorry for not texting night</marquee></h1>')
