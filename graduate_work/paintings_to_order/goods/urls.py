from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('goods', views.goods, name='goods'),
    path('product', views.product, name='product'),
]
