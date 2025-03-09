from rest_framework import serializers
from order_manager.models import Order


class OrderListSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Order. Преобразует данные
    из полей таблицы в JSON формат"""
    class Meta:
        model = Order
        fields = [
            'id',
            'table_number',
            'items',
            'total_price',
            'status',
        ]
