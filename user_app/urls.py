from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('manage-shipping/', views.manage_shipping, name='manage_shipping'),
    path('track-orders/', views.track_orders, name='track_orders'),
]