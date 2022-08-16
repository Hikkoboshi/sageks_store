from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product
from .basket import Basket
from .forms import BasketAddProductForm


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    path = request.POST.get('path', '/')
    return redirect(path)


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.remove(product)
    return redirect('basket_detail')


def basket_detail(request):
    basket = Basket(request)
    basket_product_form = BasketAddProductForm
    context = {
        'basket': basket,
        'basket_product_form': basket_product_form
    }
    return render(request, 'sageks_store/basket/basket.html', context)
