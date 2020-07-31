from django.contrib import admin
from .models import *
from django.http import HttpResponseRedirect
from django.urls import path


#Table View for Products In admin pannel
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    change_list_template = "reports.html"
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
    
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('reports/', self.set_immortal),
        ]
        return my_urls + urls

    def set_immortal(self, request):
        return HttpResponseRedirect("../")

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
