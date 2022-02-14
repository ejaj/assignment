from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet
from currency.serializers import CurrencySerializer
from currency.models import Currency


class CurrencyModelViewSet(ModelViewSet):
    """
     Currency Model View Set
    """

    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)


