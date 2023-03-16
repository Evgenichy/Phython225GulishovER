from django.db import models
from django.contrib.auth.models import User


class Cards(models.Model):
    card_name = models.CharField(max_length=50, blank=False)
    card_photo = models.ImageField(upload_to='cards/images/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.card_name}'


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

