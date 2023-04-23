from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('goods', views.goods, name='goods'),
    path('success', views.success, name='success'),
    path('product/<str:pk>/', views.product, name='product'),
    # path('comment/<str:pk>/', views.product, name='comment'),


]

