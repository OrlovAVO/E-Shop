from django.shortcuts import render


def index(request):

    context = {
        'title': 'E-Shop - Главная',
        'content': 'Магазин электротехники - E-Shop',

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
