from django.urls import path, include
from rest_framework import routers

from apis.currency.views import CurrencyModelViewSet

router = routers.DefaultRouter()
router.register('', CurrencyModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
