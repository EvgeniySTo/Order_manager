from django.db import models


STATUSES = [
    ('в ожидании', 'в ожидании'),
    ('готов', 'готов'),
    ('оплачено', 'оплачено'),
]


class Order(models.Model):
    """Модель таблицы БД. Включает в себя название полей таблицы,
    типы данных, которые необходимо вносить в поля, а так же дополнительные
    параметры ввода(максимальное количество символов, варианты для ввода и т.д.)"""
    table_number = models.PositiveIntegerField()
    items = models.CharField(max_length=500)
    total_price = models.PositiveIntegerField()
    status = models.CharField(max_length=15, choices=STATUSES)
