from django.contrib import admin
from . models import BuyAddress, Order, OrderItem

# Register your models here.

admin.site.register(BuyAddress)
admin.site.site_header = "ThrxFit Admin"
admin.site.site_title = "ThrxFit Admin Portal"
admin.site.index_title = "Welcome to ThrxFit Admin Portal"
admin.site.site_url = None

admin.site.register(OrderItem)

admin.site.register(Order)
