from django.forms import ModelForm
from .models import Order
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


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
