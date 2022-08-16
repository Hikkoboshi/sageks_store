import uuid

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Order, OrderItem
from .forms import OrderCreateForm, OrderStatusForm
from basket.basket import Basket


def order_create(request):
    basket = Basket(request)
    if not basket:
        return redirect('product_list')
    else:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid() and basket:
                order = form.save()
                for item in basket:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                # очистка корзины
                basket.clear()
                return render(request, 'sageks_store/order/created.html',
                              {'order': order})
        else:
            form = OrderCreateForm
        return render(request, 'sageks_store/order/create.html',
                      {'basket': basket, 'form': form})


def order_status(request):
    if request.method == 'POST':
        form = OrderStatusForm(request.POST)
        try:
            order_id = uuid.UUID(form.cleaned_data['order_id'])
            if form.is_valid():
                order = get_object_or_404(Order, pk=order_id)
                return render(request, 'sageks_store/order/status_detail.html', {'order': order})
        except:
            messages.warning(request, 'Такого заказа не существует или Вы ввели неправильный номер заказа.')
            return render(request, 'sageks_store/order/status_detail.html')
    else:
        form = OrderStatusForm
    return render(request, 'sageks_store/order/status.html', {'form': form})
