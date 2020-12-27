from django.db import models
from ..country.models import Country
from ..account.models import Profile

# Create your models here.


class Type(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    enable = models.BooleanField()


class State(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    enable = models.BooleanField()
    id_state = models.ForeignKey(Type, on_delete=models.CASCADE)


class Currency(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=50)
    id_state = models.ForeignKey(State, verbose_name="State", on_delete=models.CASCADE)


class Bank(models.Model):
    name = models.CharField(max_length=50)
    id_country = models.ForeignKey(
        Country, verbose_name="Country", on_delete=models.CASCADE
    )
    id_state = models.ForeignKey(State, verbose_name="State", on_delete=models.CASCADE)


class Bank_Account(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    date_edited = models.DateField(auto_now=True, auto_now_add=False)
    id_state = models.ForeignKey(State, verbose_name="State", on_delete=models.CASCADE)
    id_profile = models.ForeignKey(
        Profile, verbose_name="Profile", on_delete=models.CASCADE
    )


class Transaction(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    img = models.ImageField(
        upload_to="transaction", height_field=None, width_field=None, max_length=None
    )
    id_currency = models.ForeignKey(
        Currency, verbose_name="Currency", on_delete=models.CASCADE
    )
    id_bank_account_sender = models.ForeignKey(
        Bank_Account,
        verbose_name="Sender",
        on_delete=models.DO_NOTHING,
        related_name="Sender",
    )
    id_bank_account_receiver = models.ForeignKey(
        Bank_Account,
        verbose_name="Receiver",
        on_delete=models.DO_NOTHING,
        related_name="receiver",
    )

    id_transaction_type = models.ForeignKey(
        Type, verbose_name="Type", on_delete=models.CASCADE
    )
    id_transaction_state = models.ForeignKey(
        State, verbose_name="State", on_delete=models.CASCADE
    )
