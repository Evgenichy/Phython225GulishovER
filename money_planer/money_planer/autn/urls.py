from django.urls import path
from . import views

app_name = 'autn'

urlpatterns = [
    path('', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    # path('current/', views.currentauth, name='currentauth'),
]