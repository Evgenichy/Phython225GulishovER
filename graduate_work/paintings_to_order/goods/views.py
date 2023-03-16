from django.shortcuts import render, redirect
from .models import Cards, Size, Price


def index(request):
    return render(request, 'goods/index.html')


def goods(request):
    cards = Cards.objects.all()
    return render(request, 'goods/goods.html', {'cards': cards})


def product(request):
    return render(request, 'goods/product.html')


def select_size(request):
    sizes = Size.objects.all()
    context = {'size': sizes}
    return render(request, 'goods/product.html', context)


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



