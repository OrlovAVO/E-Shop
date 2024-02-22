from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'E-Shop - Главная',
        'content': 'Магазин электротехники - E-Shop',
        'categories': categories

    }
    return render(request, 'app/index.html', context)


def about(request):
    context = {
        'title': 'E-Shop - О нас',
        'content': 'О нас',
        'text_on_page': 'Наша цель - сделать простым доступ к огромному количеству качественных и недорогих товаров,'
                        'предоставляя лучший сервис'
    }
    return render(request, 'app/about.html', context)
