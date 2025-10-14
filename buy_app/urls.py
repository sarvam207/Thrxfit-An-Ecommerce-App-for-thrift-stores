from django.urls import path
from . import views

urlpatterns = [
    path('buy-success/', views.buy_success, name='buy_success'),
    path('buy-failed/', views.buy_failed, name='buy_failed'),
    
]