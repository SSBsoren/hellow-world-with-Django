from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def MainPage(request):
    return HttpResponse('JoharGe means Hello in Jharkhand')
