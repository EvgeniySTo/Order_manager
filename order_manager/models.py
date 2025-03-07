from django.db import models


STATUSES = [
    ('в ожидании', 'в ожидании'),
    ('готов', 'готов'),
    ('оплачено', 'оплачено'),
]


class Order(models.Model):
    table_number = models.PositiveIntegerField()
    items = models.CharField(max_length=500)
    total_price = models.PositiveIntegerField()
    status = models.CharField(max_length=15, choices=STATUSES)


class Revenue(models.Model):
    total_summ = models.PositiveIntegerField()
