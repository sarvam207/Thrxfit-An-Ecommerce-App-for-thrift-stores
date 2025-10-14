from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BuyAddress(models.Model):
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    

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
    
