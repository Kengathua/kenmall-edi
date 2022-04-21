"""Order model serializers field."""
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import PurchaseOrderAddresses, PurchaseOrder
from . import models

class PurshaseOrderSerializer(ModelSerializer):
    """PurshaseOrder model serializer."""
    created_by = serializers.UUIDField()
    billing_address = serializers.ReadOnlyField()
    shipping_address = serializers.ReadOnlyField()

    class Meta:
        """Meta class for PurshaseOrderSerializer."""

        model = PurchaseOrder
        fields = "__all__"


class PurchaseOrderAddressesSerializer(ModelSerializer):
    """PurchaseOrderAddresses model serializer."""
    created_by = serializers.UUIDField()

    class Meta:
        """Meta class for PurchaseOrderAddressesSerilizer."""

        model = PurchaseOrderAddresses
        fields = "__all__"


class PurchasesOrderItemSerializer(ModelSerializer):
    """PurchasesOrderItem model serializer."""
    created_by = serializers.UUIDField()
    class Meta:
        """Meta class for PurchasesOrderItemSerializer."""

        model = models.PurchasesOrderItem
        fields = "__all__"
