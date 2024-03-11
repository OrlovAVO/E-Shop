from django.shortcuts import render

from users.forms import UserLoginForm
def login(request):
    form = UserLoginForm()
    context = {
        'title': 'E-Shop - Авторизация',
        'form': form

    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'E-Shop - Регистрация'

    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'E-Shop - Кабинет'

    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...
