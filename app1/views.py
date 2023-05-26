from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def praveen(request):
    return HttpResponse('praveen is a human searching for meaning in life')
def kushal(request):
    return HttpResponse('searching for girls')