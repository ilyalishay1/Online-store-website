from django.db import models


class UserOrderModel(models.Model):
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    CVV = models.CharField(max_length=3)
    owner_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.owner_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



