from django.urls import path, include
from apis.views import (
    HelloApiView
)

urlpatterns = [
    path('', HelloApiView.as_view(), name="hello"),
    path('user/', include('apis.user.urls')),
    path('currencies/', include('apis.currency.urls'))
]