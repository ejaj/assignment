from rest_framework.response import Response
from rest_framework import views


class HelloApiView(views.APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
