"""EDI Debit side model serializers file."""
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from kenmall_edi.debit.models import Units


class UnitsSerializer(ModelSerializer):
    """Serializer class for the Units model."""
    created_by = serializers.UUIDField()

    class Meta:
        """Meta class for UnitsSerializer."""

        model = Units
        fields = '__all__'
