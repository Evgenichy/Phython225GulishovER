from django.db import models


class Cards(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    card_name = models.CharField(max_length=50)
    card_photo = models.ImageField(upload_to='cards/images/', default='default.jpg')
    description = models.TextField(blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.card_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Size(models.Model):
    picture_size = models.CharField(max_length=20)

    def __str__(self):
        return self.picture_size

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Order(models.Model):
    size = models.ManyToManyField(Size, blank=True, verbose_name='Размер')
    order_fio = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=12, verbose_name='Телефон')
    order_email = models.CharField(max_length=200, verbose_name='Email')
    order_photo = models.ImageField(null=True, blank=True, verbose_name='Фотография для картины')

    def __str__(self):
        return self.order_email

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


