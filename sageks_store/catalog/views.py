from django.shortcuts import render, get_object_or_404

from .models import *
from basket.forms import BasketAddProductForm


def product_list(request, category_slug=None):
    category = None
    try:
        query = request.GET.get('q')
    except:
        query = None
    products = Product.objects.filter(available=True)
    if query:
        products = products.filter(name__icontains=query.capitalize())
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    basket_product_form = BasketAddProductForm
    context = {
        'category': category,
        'query': query,
        'products': products,
        'basket_product_form': basket_product_form
    }
    return render(request, 'sageks_store/catalog/catalog.html', context)


def search(request):
    pass


def product_page(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    basket_product_form = BasketAddProductForm
    context = {
        'product': product,
        'basket_product_form': basket_product_form
    }
    return render(request, 'sageks_store/catalog/product.html', context)
