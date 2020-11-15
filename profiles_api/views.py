from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP method as function (GET, POST, PATCH, PUT, DELETE) ',
        'Is similar to a tradtional Django View ',
        'Is mapped manually to URLs',
        ]

        return Response({'message' : 'Hello World', 'an_apiview': an_apiview })

    def post(self, request):
        """ Creates a message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message =f'Hello, {name}'

            return Response({ 'message':message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def put(self, request, pk=None):
        """ Handles Full Updating of an object """

        return Response({ 'message': 'Simple PUT'})

    def  patch(self, request, pk=None):
        """ Handles partial Updating of an object """

        return Response({ 'message': 'Simple PATCH'})

    def  delete(self, request, pk=None):
        """ Handles the Deleting of an object """

        return Response({ 'message': 'Simple DELETE'})
