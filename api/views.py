from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import OrderListSerializer
from order_manager.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()



