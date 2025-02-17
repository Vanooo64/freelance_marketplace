from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Сторінка додатку замовників")


def categories(request):
    return HttpResponse("<h1>Замовленя по категоріям</h1>")
