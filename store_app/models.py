from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True) # db_index for faster lookups
    slug = models.SlugField(max_length=100, unique=True) #slug is unique for each category 
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    brand = models.CharField(max_length=200, db_index=True, default='Generic')
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
#   image = models.ImageField(upload_to='/images', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        # index_together = (('name', 'slug'),) # for faster lookups using both id and slug
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name