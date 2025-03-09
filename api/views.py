from order_manager.models import Order
from .serializers import OrderListSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class OrdersViewSet(ModelViewSet):
    """Контроллер для отображения API. Поддерживает операции отображения,
    добавления, удаления и изменения данных из БД"""
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['table_number', 'status']
