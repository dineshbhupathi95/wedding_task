from django.contrib import admin
from .models import *


#Table View for Products In admin pannel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    date_heirarchy = (
        'modified',
    )
    list_display = (
        'id',
        'name',
        'brand',
        'price',
        'in_stock_quantity',
    )

# Table view for guests admin pannel
@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    date_heirarchy = (
        'modified',
    )
    list_display = (
        'id',
        'name',
        'gift_products',
    )

# Table view for Purchase Prodcts admin pannel
@admin.register(Purchase)
class PurchaseProductsAdmin(admin.ModelAdmin):
    date_heirarchy = (
        'modified',
    )
    list_display = (
        'id',
        'product',
        'quantity',
        'purchase_date',
    )