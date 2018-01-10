from django.db import models
from django.contrib.auth.models import User

class Users(User):
    """Информация о пользователе"""
    photo = models.ImageField(blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    password = models.P
    phone = models.CharField(max_length=20, blank=True)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def name_default():
        return ' '

class Store(models.Model):
    """Магазин и информация о нем"""
    name = models.CharField(max_length=50)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)

class Address(models.Model):
    address = models.CharField(max_length=100)

class Stock(models.Model):
    """Склад"""

class Port(models.Model):
    """Порт продавца"""
    port = models.CharField(max_length=10)
    text = models.TextField(blank=True)
    user = models.ForeignKey(Users, default="No name")

class Order(models.Model):
    """Заказ"""
    date_added = models.DateTimeField(auto_now_add=True)
    accepted = models.ForeignKey(User, default='No name')

    def __str__(self):
        return '{}, {}'.format(self.accepted,
                               self.date_added)

class Customer(models.Model):
    """Информация по заказчику"""
    order = models.ForeignKey(Order)
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    telephon = models.CharField(max_length=20,
                                blank=True)
    email = models.EmailField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    comments = models.TextField(blank=True)

class Order(models.Model):
    port = models.CharField(max_length=10)
    seller = models.CharField()
    text = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


# Create your models here.
