from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.forms.models import ModelForm
from phonenumber_field.modelfields import PhoneNumberField
from products.models import Product, ProductVariant, ProductImage
from django.core.validators import RegexValidator
from django.utils.text import gettext_lazy as _

class Province(models.Model):
    acronym = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f'{self.name}'


class PaymentMethod(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField("Nome completo (nome e cognome)", max_length=40)
    phone_number = PhoneNumberField("Numero di telefono", region="IT")
    address_line_one = models.CharField("Riga Indirizzo 1", max_length=40)
    address_line_two = models.CharField("Riga Indirizzo 2", max_length=40, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.PROTECT)
    postal_code = models.CharField("CAP", max_length=5, validators = [RegexValidator('^[0-9]{5}$', _('CAP non valido, inserisci 5 numeri'))])
    city = models.CharField("city", max_length=40)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)

    @property
    def total_price(self):
        return sum(product.price * product.quantity for product in OrderItem.objects.filter(order=self))
    # remove possibility to change order after shipping
    # before shipping it's possible to add OrderProducts to the order and create new payments to pay the OrderProducts
    # the payment class should mark which OrderProducts are paid


class OrderItem(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE, editable=False)
    variant = models.ForeignKey('products.ProductVariant', on_delete=models.PROTECT, editable=False)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    @property
    def name(self):
        return self.variant.product.name

    @property
    def total_price(self):
        return self.price * self.quantity

    @property
    def default_image(self):
        return self.variant.default_image


    def save(self, *args, **kwargs):
        if self._state.adding:
            self.price = self.variant.discounted_price

        super(OrderItem, self).save(*args, **kwargs)
