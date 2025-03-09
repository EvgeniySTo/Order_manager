from django.urls import path, include
from api.views import OrdersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orders', OrdersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
