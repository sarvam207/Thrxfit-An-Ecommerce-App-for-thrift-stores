from django.contrib import admin
from django.urls import include

from django.urls import path

from . import views

urlpatterns = [
    # Store main page
    path('', views.store_app, name='store_app'),
    # Individual product
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
    # Individual category
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
]