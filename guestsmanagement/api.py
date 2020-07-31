from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
import io
import csv
from django.http import HttpResponse



# Create Guests and List Of guests
class GuestsApi(ListCreateAPIView):
    serializer_class = guestsSerializer
    queryset = Guest.objects.all()

# create products(gifts) and list of gifts
class ProductsApi(ListCreateAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

#Retrieve and update and delete api for signle product(gift) object
class ProductDatailsView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

#create and List of Puchased Products(gifts) and it will update products quantity which will puchase
class PurchaseProductsApi(ListCreateAPIView):
    serializer_class = PurchaseProductsSerializer
    queryset = Purchase.objects.all()

    def post(self, request, *args, **kwargs):
        #taking quanttiy
        quantity = request.data['quantity']
        #taking product object id
        product_id = request.data['product']
        #with product id filtering product object
        products_queryset = Product.objects.filter(id=product_id).values('in_stock_quantity')
        for product in products_queryset:
            update_quantity = product['in_stock_quantity']+int(quantity)
            print(update_quantity,'lll')
            # updating product qunatity
            Product.objects.filter(id=product_id).update(in_stock_quantity=update_quantity)
        return self.create(request, *args, **kwargs)

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gifts.csv"'

    writer = csv.writer(response)
    writer.writerow(['product Name', 'Prand', 'Price', 'Quantity'])

    gifts = Product.objects.all().values_list('name', 'brand', 'price', 'in_stock_quantity')
    for user in gifts:
        writer.writerow(user)

    return response