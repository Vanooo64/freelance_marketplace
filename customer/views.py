from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = [{'title': 'Про сайт', 'url_name': 'about'},
        {'title': 'Додати роботу', 'url_name': 'add_order'},
        {'title': 'Зворотній звя`зок', 'url_name': 'contact'},
        {'title': 'Увійти', 'url_name': 'login'},
    ]


data_db = [
    {'id': 1, 'type': 'Курсова', 'title': 'Написати курсову работу', 'description': "Курсова робота перевірятиметься на плагіат в Антиплагіат ВУЗ.", 'is_published': True},
    {'id': 1, 'type': 'Дипломна', 'title': 'Написати диплдомну работу', 'description': "Особливості нормативно-правових актів у сфері правового регулювання фінансового контролю.", 'is_published': True},
    {'id': 3, 'type': 'Реферат', 'title': 'Написати реферат', 'description': "Загальна характеристика фінансового контролю та його правової регламентації", 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Дипломи'},
    {'id': 2, 'name': 'Курсові'},
    {'id': 3, 'name': 'Реферати'},
    {'id': 4, 'name': 'Єссе'},
]

def index(request):
    data = {'title': 'Головна сторінка',
            'menu': menu,
            'orders': data_db,
            'cat_selected': 0
    }
    return render(request, "customer/index.html", context=data)


def about(request):
    return render(request, "customer/about.html", {'title': 'Про сайт', 'menu': menu})



def show_order(request, order_id):
    return HttpResponse(f"Робота з id: {order_id}")


def addorder(request):
    return HttpResponse("Додавання статі")

def contact(request):
    return HttpResponse("Зворотній звязок")

def login(request):
    return HttpResponse("Авторизуватися")

def show_category(request, cat_id):
    data = {'title': 'Відтворення по рубрикам',
            'menu': menu,
            'orders': data_db,
            'cat_selected': cat_id,
            }
    return render(request, "customer/index.html", context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Сторінка не знайдена</h1>")


