from django.db import models
from django.contrib.auth.models import User

from store_app.models import Product

# Create your models here.
class BuyAddress(models.Model):
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=350, blank=True, null=True)
    
    #optional fields
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    
    #foriegn key user
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    
    class Meta:
        verbose_name = 'Shipping Address'
        verbose_name_plural = 'Shipping Address'
        
    def __str__(self):
        return 'Shipping Address -' + str(self.id)
    

class Order(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    shipping_address = models.TextField(max_length=900)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    
    #foriegn key product
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return 'Order- #' + str(self.id)

class OrderItem(models.Model):
    #foriegn key user
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.CASCADE, null=True, blank=True)

    #foriegn key order
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, null=True, blank=True)
    
    #foriegn key product
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return 'Order Item - #' + str(self.id)
