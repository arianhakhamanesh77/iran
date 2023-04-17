from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    category = models.ForeignKey(to='CategoryModel', on_delete=models.CASCADE, related_name='productSet')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    best_offer = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='productImage')
    score = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))

    def __str__(self):
        return self.name


class AdsModel(models.Model):
    avatar = models.ImageField(upload_to='AdsImage')
    text = models.CharField(blank=True, max_length=255)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class HotOfferModel(models.Model):
    product = models.ForeignKey(to='ProductModel', on_delete=models.CASCADE)
    discount = models.IntegerField()
    new_price = models.IntegerField()
    time = models.DateTimeField()
    is_publish = models.BooleanField(default=False)
    banner = models.ImageField(upload_to='bannerImage')

    def __str__(self):
        return self.product.name


class BestProductModel(models.Model):
    product = models.ForeignKey(to='ProductModel', on_delete=models.PROTECT)
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.product.name
