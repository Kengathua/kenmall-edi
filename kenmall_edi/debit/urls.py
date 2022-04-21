"""Urls file for EDI debit side views."""

from rest_framework import routers
from django.urls import path, include

from kenmall_edi.debit.views import (
    UnitsViewSet)

router = routers.DefaultRouter()

router.register(r'units', UnitsViewSet)

urlpatterns = [
    path('debit_side/', include(router.urls)),
]