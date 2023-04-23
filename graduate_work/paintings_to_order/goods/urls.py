from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback', views.feedback, name='form_order'),
    path('goods', views.goods, name='goods'),
    path('product/<str:pk>/', views.product, name='product'),
    path('contacts', views.contacts, name='contacts'),
    path('about_order', views.about_order, name='about_order'),
]
