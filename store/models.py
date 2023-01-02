from django.db import models
from core.models import Profile

# Current user model in use
""" from django.contrib.auth import get_user_model
User = get_user_model() """


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50, blank=False)
    item_price = models.IntegerField(blank=True)
    item_quantity_received = models.IntegerField(blank=False)
    item_quantity_available = models.IntegerField(blank=True)
    item_purchased_date = models.DateField(auto_now_add=True, blank=False)
    item_units = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.item_name


class Broken(models.Model):
    item = models.ForeignKey(Item, default=1,  on_delete=models.CASCADE)
    item_quantity_broken = models.IntegerField(blank=True)
    item_broken_date = models.DateField(auto_now_add=True, blank=False)
    item_is_broken = models.BooleanField(default=True)
    date_repaired = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.item.item_name


class Lend(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_quantity_lent = models.IntegerField(blank=True)
    item_lent_date = models.DateField(auto_now_add=True, blank=False)
    item_is_lent = models.BooleanField(default=True)
    date_returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return (self.item.item_name)
