from django.urls import path, re_path, register_converter
from customer import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('order/<int:order_id>/', views.order, name="order_id"),
    path('order/<slug:order_slug>/', views.order_by_slug, name = "orders"),
    path("archive/<year4:year>/", views.archive, name = "archive"),
]