from django.shortcuts import render, redirect, get_object_or_404

from carts.models import Cart
from goods.models import Products


def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    if request.method == 'POST':
        action = request.POST.get("action")  # Получение значения action из запроса

        cart_item = get_object_or_404(Cart, product__slug=product_slug)

        if action == 'add':
            cart_item.quantity += 1
            cart_item.save()

        elif action == 'remove':  # Используйте elif вместо if, чтобы проверить разные действия
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()

        return redirect(request.META['HTTP_REFERER'])

    else:
        return redirect(request.META['HTTP_REFERER'])