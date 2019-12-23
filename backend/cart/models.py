from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s'%(self.name, self.price)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through='Item')

    # @classmethod
    # def create(cls, customer)

    def __str__(self):
        return self.customer.username

class Item(models.Model):
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_item = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_item.name
