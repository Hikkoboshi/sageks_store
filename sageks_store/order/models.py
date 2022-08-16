import uuid

from django.db import models
from catalog.models import Product


class Order(models.Model):
    DELIVERY = (
        ('Самовывоз', 'Самовывоз'),
        ('Доставка', 'Доставка')
    )
    STATUS = (
        ('Обрабатывается', 'Обрабатывается'),
        ('Принят', 'Принят'),
        ('В пути', 'В пути'),
        ('Завершен', 'Завершен')
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(verbose_name='Имя', max_length=50)
    email = models.EmailField(verbose_name='Почта', )
    delivery = models.CharField(verbose_name='Способ доставки', default=DELIVERY[1][0], max_length=20, choices=DELIVERY)
    city = models.CharField(verbose_name='Город', max_length=100)
    address = models.CharField(verbose_name='Адрес', max_length=250)
    status = models.CharField(verbose_name='Статус', default=STATUS[0][0], null=True, max_length=20, choices=STATUS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    @property
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    @property
    def get_cost(self):
        return self.price * self.quantity
