from django.forms import ModelForm
from .models import Order, ComForm
from django import forms


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['order_fio', 'order_phone', 'order_email', 'order_photo', 'size']

        widgets = {
            'size': forms.CheckboxSelectMultiple(),
        }


class FeedbackForm(ModelForm):
    class Meta:
        model = Order
        fields = ['order_fio', 'order_phone', 'order_email']


class CommentForm(forms.ModelForm):
    class Meta:
        model = ComForm
        fields = ['email', 'name', 'text_com']

        labels = {
            'name': 'Имя',
            'text_com': 'Напишите отзыв...'
        }

