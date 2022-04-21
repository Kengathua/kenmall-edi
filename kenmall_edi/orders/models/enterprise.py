"""EDI enterprise orders file"""
from django.db import models
from django.utils import timezone

from kenmall_edi.common.models import AbstractBase
from kenmall_edi.users.models import retrieve_user_email

PURSCHASE_ORDER_STATUS_CHOICES = (
    ('PENDING', 'PENDING'),
    ('PROCESSING', 'PROCESSING'),
    ('CANCELLED', 'CANCELLED'),
    ('FULFILLED', 'FULFILLED'),
)

PENDING = 'PENDING'


class PurchaseOrder(AbstractBase):
    guid = models.UUIDField()
    customer_kenmall_code = models.CharField(max_length=300, null=True, blank=True)
    customer_name = models.CharField(max_length=300, null=False, blank=False)
    vendor_kenmall_code = models.CharField(max_length=300, null=True, blank=True)
    vendor_name = models.CharField(max_length=300, null=False, blank=False)
    order_number = models.CharField(max_length=300, null=False, blank=False)
    subject = models.CharField(max_length=300, null=True, blank=True)
    requisition_no = models.CharField(max_length=300,null=True, blank=True)
    tracking_number = models.CharField(max_length=300,null=True, blank=True)
    contact_name = models.CharField(max_length=300, null=True, blank=True)
    sales_person = models.CharField(max_length=300, null=True, blank=True)
    carrier = models.CharField(max_length=300, null=True, blank=True)
    order_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    excise_duty = models.FloatField(null=True, blank=True)
    sales_commission = models.FloatField(null=True, blank=True)
    status = models.CharField(
        choices=PURSCHASE_ORDER_STATUS_CHOICES,
        max_length=300, default=PENDING)
    assigned_to = models.CharField(max_length=300, null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    list_price = models.FloatField(null=True, blank=True)
    subtotal_amount = models.FloatField(null=True, blank=True)
    discount_amount = models.FloatField(null=True, blank=True)
    terms_and_conditions = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    creator = retrieve_user_email('created_by')
    updater = retrieve_user_email('updated_by')

    @property
    def billing_address(self):
        address = PurchaseOrderAddresses.objects.get(id=self.billing_address_id)
        biller_name = ''
        street = address.street
        postal_address = address.postal_address
        town = address.town
        county = address.county
        town_code = address.town_code
        country = address.country

        address_ = {
            'biller_name': biller_name,
            'street': street,
            'postal_address': postal_address,
            'town_code': town_code,
            'town': town,
            'county': county,
            'country': country,
        }

        return address_

    @property
    def shipping_address(self):
        address = PurchaseOrderAddresses.objects.get(id=self.shipping_address_id)
        client_name = ''
        street = address.street
        postal_address = address.postal_address
        town = address.town
        county = address.county
        town_code = address.town_code
        country = address.country

        address_ = {
            'biller_name': client_name,
            'street': street,
            'postal_address': postal_address,
            'town_code': town_code,
            'town': town,
            'county': county,
            'country': country,
        }

        return address_


class PurchasesOrderItem(AbstractBase):
    guid = models.UUIDField()
    purchase_order_guid = models.UUIDField()
    code = models.CharField(max_length=300)
    product_name = models.CharField(max_length=300, null=True, blank=True)
    product_description = models.CharField(
        null=True, blank=True, max_length=300)
    quantity = models.FloatField()
    unit_price = models.DecimalField(max_digits=30, decimal_places=2)
    unit_discount = models.DecimalField(
        max_digits=30, decimal_places=2, default=0)
    discount_amount = models.DecimalField(
        max_digits=30, decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=30, decimal_places=2)

    def clean(self) -> None:
        return super().clean()


class PurchaseOrderAddresses(AbstractBase):
    street = models.CharField(max_length=300)
    town = models.CharField(max_length=300)
    county = models.CharField(max_length=300)
    town_code = models.CharField(max_length=300)
    postal_address = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
