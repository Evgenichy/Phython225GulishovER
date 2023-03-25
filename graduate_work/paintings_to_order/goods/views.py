from django.shortcuts import render, redirect
from .models import Cards
from .forms import Order, OrderForm


def index(request):
    return render(request, 'goods/index.html')


def goods(request):
    cards = Cards.objects.all()
    return render(request, 'goods/goods.html', {'cards': cards})


def product(request, pk):
    card_name = Cards.objects.get(id=pk)
    order_form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILE)
        if form.is_valid():
            form.save()

    return render(request, 'goods/product.html', {'card_name': card_name, 'order_form': order_form})


# def feedback(request):
#     return render(request, 'good/feedback.html')

# def basket(request):
#     basket = Basket.objects.filter(user=request.user).first()
#
#     if basket == None:
#         basket = Basket.objects.create(user=request.user)
#
#     basket.products.add(product)
#
#     return redirect('product_detail', product_pk=product.pk)



