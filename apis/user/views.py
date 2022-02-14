from rest_framework.response import Response
from rest_framework import views, permissions, status, generics

from apis.user.serializers import (
    UserRegistrationSerializer
)


class UserRegistrationAPIView(generics.GenericAPIView):
    """
    User Registration Api View
    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        """
        Handle post request
        :param request:
        :return:
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)