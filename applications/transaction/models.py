from django.db import models
from ..shared.models import Country, State, Type
from ..account.models import Profile

# Create your models here.


class Currency(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=50)
    state = models.ForeignKey(State, verbose_name="State", on_delete=models.CASCADE)


class Bank(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country, verbose_name="Country", on_delete=models.CASCADE
    )
    state = models.ForeignKey(State, verbose_name="State", on_delete=models.CASCADE)


class Bank_Account(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    date_edited = models.DateField(auto_now=True, auto_now_add=False)
    state = models.ForeignKey(State, verbose_name="State", on_delete=models.CASCADE)
    user_profile = models.ForeignKey(
        Profile, verbose_name="Profile", on_delete=models.CASCADE
    )


class Transaction(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    img = models.ImageField(
        upload_to="transaction", height_field=None, width_field=None, max_length=None
    )
    currency = models.ForeignKey(
        Currency, verbose_name="Currency", on_delete=models.CASCADE
    )
    bank_account_sender = models.ForeignKey(
        Bank_Account,
        verbose_name="Sender",
        on_delete=models.DO_NOTHING,
        related_name="Sender",
    )
    bank_account_receiver = models.ForeignKey(
        Bank_Account,
        verbose_name="Receiver",
        on_delete=models.DO_NOTHING,
        related_name="receiver",
    )

    transaction_type = models.ForeignKey(
        Type, verbose_name="Type", on_delete=models.CASCADE
    )
    transaction_state = models.ForeignKey(
        State, verbose_name="State", on_delete=models.CASCADE
    )
