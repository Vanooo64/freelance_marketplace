from django.urls import path, re_path, register_converter
from customer import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('addorder/', views.addorder, name="add_order"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('order/<int:order_id>/', views.show_order, name="order"),
    path('category/<int:cat_id>/', views.show_category, name="category")
]