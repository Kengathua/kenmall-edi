from django.db import models
from django.db.models import PROTECT

from kenmall_edi.common.models import AbstractBase


class Units(AbstractBase):
    section = models.CharField(max_length=300)
    category = models.CharField(max_length=300)  # TV, Fridge
    units_name = models.CharField(
        null=False, blank=False, max_length=300)
    units_code = models.CharField(
        null=True, blank=True, max_length=250)

    def clean(self) -> None:
        return super().clean()


    class Meta:
        """Meta class dor item measure units."""

        ordering = ['-created_on','-units_name']
