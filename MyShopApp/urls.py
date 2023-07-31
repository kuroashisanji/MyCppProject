from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkoutView, name="checkoutView"),
    path("acknowledgement/", views.acknowledgementView, name="acknowledgement"),
    path('search/', views.search_results, name='search_results'),
]
