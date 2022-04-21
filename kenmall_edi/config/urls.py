"""kenmall_edi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


v1_patterns = [
    path(r'', include(
        ('kenmall_edi.orders.urls', 'orders'), namespace='orders')),
    path(r'', include(
        ('kenmall_edi.debit.urls', 'debit'), namespace='debit')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'v1/', include((v1_patterns, 'v1'), namespace='v1')),
]
