from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'E-Shop - Каталог'
    }
    return render(request, 'goods/catalog.html')


def product(request):
    return render(request, 'goods/product.html')
