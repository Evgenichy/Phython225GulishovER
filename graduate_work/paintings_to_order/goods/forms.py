from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['order_fio', 'order_phone', 'order_email', 'order_photo']
