from .basket import Basket


def load_basket(request):
    basket = Basket(request)
    return {
        'basket': basket,
    }
