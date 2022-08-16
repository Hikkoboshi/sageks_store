from customer.models import Customer
from basket.models import Basket

import uuid


def session(request):
    try:
        customer = Customer.objects.get(session=request.COOKIES['sessionid'])
        basket = Basket.objects.get(customer=customer, completed=False)
    except:
        customer = Customer.objects.create(session=request.COOKIES['sessionid'])
        basket = Basket.objects.create(customer=customer, completed=False)

    return {'basket': basket, 'customer': customer}
