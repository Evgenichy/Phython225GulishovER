from django.db import models


class Mapp(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='mapp/images/')
    url = models.URLField(blank=True)
