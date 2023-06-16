from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","description","price","created_at","category",]