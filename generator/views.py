from django.shortcuts import render
from generator.models import Nickname
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def author(request):
    return render(request, 'generator/aboutauthor.html')


def get_password(request):

    sym = list('abcdefghijklmnopqrstuvwxyz')
    psw = ''

    if request.GET.get('uppercase'):
        sym.extend('abcdefghijklmnopqrstuvwxyz'.upper())

    if request.GET.get('numbers'):
        sym.extend('0123456789')

    if request.GET.get('specsymbols'):
        sym.extend('!@#$%^&*(){}|/><:;~`')

    for i in range(int(request.GET.get('length'))):
        psw += random.choice(sym)

    return render(request, 'generator/password.html', {'password': psw})
