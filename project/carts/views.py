from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from carts.models import Cart
from goods.models import Products


@login_required()
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
        action = request.POST.get("action")

        cart_item = get_object_or_404(Cart, product__slug=product_slug)

        if action == 'add':
            cart_item.quantity += 1
            cart_item.save()

        elif action == 'remove':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()

        return redirect(request.META['HTTP_REFERER'])

    else:
        return redirect(request.META['HTTP_REFERER'])