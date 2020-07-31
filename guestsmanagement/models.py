from django.db import models

# Guest Table
class Guest(models.Model):
    name = models.CharField(max_length=50)
    gift_products = models.ForeignKey("guestsmanagement.Product", on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)

#Products(Gifts) Table
class Product(models.Model):
    name = models.CharField(max_length=225)
    brand = models.CharField(max_length=225)
    price = models.CharField(max_length=30,null=True,blank=True)
    in_stock_quantity = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)

#product purchse Table
class Purchase(models.Model):
    product = models.ForeignKey("guestsmanagement.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.product)