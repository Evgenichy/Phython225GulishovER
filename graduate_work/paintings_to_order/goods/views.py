from django.shortcuts import render, redirect
from .models import Cards
from .forms import OrderForm, FeedbackForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def index(request):
    return render(request, 'goods/index.html')


def feedback(request):
    feedback_form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'goods/form_order.html', {'feedback_form': feedback_form})


def goods(request):
    cards = Cards.objects.all()
    return render(request, 'goods/goods.html', {'cards': cards})


def product(request, pk):
    card_name = Cards.objects.get(id=pk)
    order_form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'goods/product.html', {'card_name': card_name, 'order_form': order_form})


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect('contacts')

    form = ContactForm()
    return render(request, 'goods/contacts.html', {'form': form})


def about_order(request):
    return render(request, 'goods/about_order.html')


