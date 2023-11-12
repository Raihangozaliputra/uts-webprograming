from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("product/", views.products, name="products"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
]