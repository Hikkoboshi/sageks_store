import uuid

from django.db import models

from catalog.models import Product
from customer.models import Customer


class Basket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.session

    @property
    def total(self):
        basket_items = self.basketitems_set.all()
        total = sum([item.subtotal for item in basket_items])
        return total

    @property
    def quantity(self):
        basket_items = self.basketitems_set.all()
        quantity = sum([item.quantity for item in basket_items])
        return quantity

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class BasketItems(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name

    @property
    def subtotal(self):
        total = self.quantity * self.product.price
        return total