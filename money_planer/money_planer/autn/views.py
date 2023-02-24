from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'autn/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()
        else:
            print('Пароли не совпадают')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'autn/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'autn/loginuser.html', {'form': AuthenticationForm(),
                                                           'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('index')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
