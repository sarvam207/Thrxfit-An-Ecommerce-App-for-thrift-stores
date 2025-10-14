from django.contrib import admin
from . models import Category, Product
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

@admin.register(Category)
class CategoryAdmin(ImportExportActionModelAdmin,admin.ModelAdmin,):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # auto fill slug field based on name field
    
@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)} # auto fill slug field based on name field
    search_fields = ['name', 'description', 'brand', 'category__name']
    ordering = ['name']