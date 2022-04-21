"""Orders urls file."""

from rest_framework import routers
from django.urls import path, include

from kenmall_edi.orders.views import(
    PurshaseOrderViewSet, PurchaseOrderAddressesViewSet)
from kenmall_edi.orders import views

e_router = routers.DefaultRouter() # router for enterprise edi views
c_router = routers.DefaultRouter() # router for customer edi views

e_router.register(r'purshases_orders', PurshaseOrderViewSet)
e_router.register(r'purshases_order_addresses', PurchaseOrderAddressesViewSet)
e_router.register(r'purshases_order_items', views.PurchaseOrderItemViewSet)


urlpatterns = [
    path('enterprise_orders/', include(e_router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
