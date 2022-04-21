from django.db import models
from django.db.models import PROTECT
from django.core.exceptions import ValidationError

from kenmall_edi.common.models import AbstractBase

KSH = 'KSH'


class Catalog(AbstractBase):
    marked_price = models.FloatField(null=True, blank=True)
    discount = models.FloatField()
    selling_price = models.FloatField(null=True, blank=True)
    currency = models.CharField(
        null=False, blank=False, max_length=250, default=KSH)
    quantity = models.FloatField()
    on_display = models.BooleanField(default=True)
    special_offer = models.CharField(null=True, blank=True, max_length=1000)
    item_name = models.CharField(null=False, blank=False, max_length=250)

    class Meta:
        """Meta class for catalog."""
        ordering = ['-marked_price', '-selling_price', '-item']
    # clean to check if item has restrictions (on_deposit)
    # clean to check if that specific item is on 
    # Add an endpoint to remove item from catalog
    # auto calculate selling price given marked price and discount
    # validate item exists in inventory