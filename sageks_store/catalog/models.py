from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=50, null=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория',  on_delete=models.SET_NULL, null=True)
    name = models.CharField(verbose_name='Название товара', max_length=100, null=True)
    price = models.FloatField(verbose_name='Цена', )
    stock = models.PositiveIntegerField(verbose_name='Остаток')
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    available = models.BooleanField(verbose_name='Доступен', default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_page',
                       args=[self.slug])

    @property
    def primary_image(self):
        image = self.productimages_set.first()
        return image

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImages(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Изображение', upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'