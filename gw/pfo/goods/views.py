from django.shortcuts import render, redirect
from .models import Goods
from .forms import OrderForm, CommentForm


def index(request):
    return render(request, 'goods/index.html')


def goods(request):
    cs = Goods.objects.all()
    context = {'cards': cs}
    return render(request, 'goods/goods.html', context)


def product(request, pk):
    product_obj = Goods.objects.get(id=pk)
    order_form = OrderForm()
    coment = CommentForm()

    context = {
        'product': product_obj,
        'order_form': order_form,
        'coment': coment,
    }

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')

    if request.method == 'POST':
        coment = CommentForm(request.POST)
        if coment.is_valid():
            coment.save(commit=False)

            return render(request, 'goods/product.html')

    return render(request, 'goods/product.html', context)


def success(request):
    return render(request, 'goods/success.html')


# def comment(request, pk):
#     com_form = Goods.objects.get(id=pk)
#     context = {
#         'coment': com_form
#     }
#
#     if request.method == 'POST':
#         com_form = CommentForm(request.POST)
#     if com_form.is_valid():
#         com_form.save()
#
#     return render(request, 'goods/product.html', context)

