from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):
    data = {'title': 'Головна сторінка'}
    return render(request, "customer/index.html", data)


def about(request):
    return render(request, "customer/about.html", {'title': 'Про сайт'})



def order(request, order_id):
    return HttpResponse(f"<h1>Замовленя по категоріям</h1><p>id: {order_id}</p>")


def order_by_slug (request, order_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Замовленя по категоріям</h1><p>slug: {order_slug}</p>")

def archive(request, year):
    if year > 2024:
        uri = reverse("orders", args=("diplom", ))
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"<h1>Архів по рокам</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Сторінка не знайдена</h1>")


