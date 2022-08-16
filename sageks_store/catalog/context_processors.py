from .models import *


def load_catalog(request):
    categories = Category.objects.all()
    return {
        'categories': categories,
    }
