import uuid

from django.db import models


class Customer(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    session = models.CharField(max_length=100, unique=True, null=True)
    email = models.EmailField(verbose_name='Почта', null=True, blank=True)
    phone = models.IntegerField(verbose_name='Телефон', null=True, blank=True)
    firstname = models.CharField(verbose_name='Имя', max_length=20, null=True, blank=True)
    lastname = models.CharField(verbose_name='Фамилия', max_length=20, null=True, blank=True)
    date_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.session

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
