from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from kenmall_edi.debit.models import (
    Units)
from kenmall_edi.debit.serializers import (
    UnitsSerializer)


class UnitsViewSet(ModelViewSet):
    """Viewset for the Units model"""
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
