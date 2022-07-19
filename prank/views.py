from unittest import skip
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template , Context
import random, time
import pyautogui as pg

    
def search(request):
    d=request.POST
    term=d['text'] 
    var=term
    time.sleep(8)
    for i in range(50):
        a= random.choice(var)
        pg.write(var)
        pg.press('enter')
    # context = {'data': var}
    return render(request, "result.html")


def index(request):
    return render(request, 'index.html')

def result(request):
    return render(request, 'result.html')
    
def contact(request):
    return render(request, 'result.html')

    
def about(request):
    return render(request, 'about.html')
