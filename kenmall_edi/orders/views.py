from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from kenmall_edi.orders.models import (
    PurchaseOrder, PurchasesOrderItem, PurchaseOrderAddresses)
from kenmall_edi.orders.serializers import (
    PurshaseOrderSerializer, PurchaseOrderAddressesSerializer)
from kenmall_edi.orders import serializers


class PurshaseOrderViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurshaseOrderSerializer


class PurchaseOrderAddressesViewSet(ModelViewSet):
    queryset = PurchaseOrderAddresses.objects.all()
    serializer_class = PurchaseOrderAddressesSerializer


class PurchaseOrderItemViewSet(ModelViewSet):
    queryset = PurchasesOrderItem.objects.all()
    serializer_class = serializers.PurchasesOrderItemSerializer
