from django.contrib import admin
from .models import User, Product, Category, Order, Item

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'created_by')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'order_item', 'quantity')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)
