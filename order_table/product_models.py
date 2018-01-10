from django.db import models

class ProductClass(models.Model):
    product_name = models.CharField(max_length=100)
    def __str__(self):
        return self.product_name

class ProductType(models.Model):
    product_types = models.CharField(max_length=100)
    def __str__(self):
        return self.product_types

class ProductName(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class ProductHeight(models.Model):
    product_height = models.IntegerField()
    def __str__(self):
        return self.product_height

class ProductWidth(models.Model):
    product_width = models.IntegerField()
    def __str__ (self):
        return self.product_width

class Colour(models.Model):
    colour = CharField(max_length=100)
    def __str__(self):
        return self.colour

class Material(models.Model):
    material_name = models.CharField(max_length=60)
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.material_name}, {self.colour}'

class Product(models.Model):
    """Products table"""
    name = models.ForeignKey(
        ProductName,
        on_delete=models.CASCADE
    )
    classes = models.ForeignKey(
        ProductClass,
        blank=True,
        on_delete=models.CASCADE
    )
    types = models.ForeignKey(
        ProductType,
        blank=True,
        on_delete=models.CASCADE
    )
    height = models.ForeignKey(
        ProductHeight,
        blank=True,
        on_delete=models.CASCADE
    )
    width = models.ForeignKey(
        ProductWidth,
        blank=True,
        on_delete=models.CASCADE
    )
    materials = models.ForeignKey(
        Material,
        blank=True,
        on_delete=models.CASCADE
    )
    notes = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    IN_THE_COLLECTION_CHOICES = [
        ('Да','Ткань есть в наличии'),
        ('Нет', 'Ткань выведенна из коллекции ')]
    in_the_collection = models.CharField(
        max_length=3,
        choices=IN_THE_COLLECTION_CHOICES,
        default='Да'
    )

    def __str__(self):
        return f'{self.id} -- {self.name} -- {self.classes} -- {self.types}'

class WareHouse(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Stock(models.Model):

    name = models.ForeignKey(
        WareHouseName,
        on_delete=models.CASCADE
    )
    products = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField(default='Нет в наличии')
