from django.db import models
from django.contrib.auth.models import User


class Cards(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    card_name = models.CharField(max_length=50)
    card_photo = models.ImageField(upload_to='cards/images/', default='default.jpg')
    description = models.TextField(blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.card_name}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)


class Size(models.Model):
    picture_size = models.CharField(max_length=20)

    def __str__(self):
        return self.picture_size


class Price(models.Model):
    picture_price = models.ForeignKey(Size, on_delete=models.CASCADE)
    list_price = models.CharField(max_length=50)

    def __str__(self):
        return self.list_price


class Order(models.Model):
    order_fio = models.CharField(max_length=200)
    order_phone = models.CharField(max_length=12)
    order_email = models.CharField(max_length=200)
    order_photo = models.ImageField(null=True, blank=True)



