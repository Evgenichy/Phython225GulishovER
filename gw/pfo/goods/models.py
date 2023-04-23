from django.db import models


class Goods(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, upload_to='goods/%Y/%m/%d', default='default.jpg')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Size(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

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


class ComForm(models.Model):
    product = models.ForeignKey(Goods, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='email')
    name = models.CharField(max_length=50)
    text_com = models.TextField(max_length=500)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'




