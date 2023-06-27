from django.contrib import admin
from .models import Category, Product,favoritos


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price','disponible', 'created', 'updated']
    list_filter = ['disponible', 'created', 'updated']
    list_editable = ['price', 'disponible']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(favoritos)
class favoritosadmin(admin.ModelAdmin):
    list_display = ['id','user','producto','creacion']
