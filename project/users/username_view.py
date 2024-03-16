from django.shortcuts import render
from users.models import User  # Импортируем вашу модель User из users.models


def my_view(request):
    context = {}
    if request.user.is_authenticated:
        user_instance = User.objects.get(pk=request.user.pk)  # Получаем экземпляр объекта User
        context['username'] = user_instance.username
    return render(request, 'basic.html', context)
