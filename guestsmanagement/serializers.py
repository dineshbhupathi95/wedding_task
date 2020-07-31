from rest_framework import serializers
from .models import *

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class guestsSerializer(serializers.ModelSerializer):
    gift_products = ProductsSerializer(required=True)
    class Meta:
        model = Guest
        fields = ["id","name","gift_products"]

class PurchaseProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"

