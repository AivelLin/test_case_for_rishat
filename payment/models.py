from django.db import models
from django.urls import reverse


class Item(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'dollars'),
        ('RUB', 'rubles'),
        ('EUR', 'euro')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, default='RUB')

    def get_price_show(self):
        return '{0:.2f}'.format(self.price / 100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_id': self.pk})
