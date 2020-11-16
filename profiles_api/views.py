from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from .serializers import HelloSerializer, UserProfileSerializer, ProfileFeedItemSerializer
from .models import  UserProfile, ProfileFeedItem
from .permissions import UpdateOwnProfile, UpdateOwnStatus

#  USING APIVIEW
class HelloApiView(APIView):
    """ Test API View """
    serializer_class = HelloSerializer

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


# USING VIEWSETS
class HelloViewSet(viewsets.ViewSet):
    """ Tests API Viewset """
    serializer_class = HelloSerializer

    def list(self, request):
        """ Returns a Hello Message """
        a_viewset = [
        'Uses actions (list, create, retrieve, update, partial_updates)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less codes'
        ]
        return Response({'message':'Hello ViewSet', 'a_viewset': a_viewset })


    def create(self, request):
        """ Creates a new Hello Message """
        serializer_class = HelloSerializer
        serializer = self.serializer_class(data=request.data)

        # Validate the serializer data
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}. This is ViewSet'
            return Response({message})

        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        """ Gets single Object by its ID """

        return Response({'message': 'This is a simple GET request from ViewSet'})

    def update(slef, request, pk=None):
        """Handles Updating a single Object """

        return Response({'message':'This is a simple PUT request from ViewSet'})

    def partial_update(self, request, pk=None):
        """ Handles Updating part of an object """

        return Response({'message': 'This is a simple PATCH request from ViewSet'})

    def delete(self, request, pk=None):
        """ Destroys object data in db """

        return Response({'message': 'This is a simple DELETE request from ViewSet'})


# User Profile ViewSet
class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handles creating and Updating user's profile """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [UpdateOwnProfile]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

# User Login APIView
class UserLoginApiView(ObtainAuthToken):
    """ Handles creating user authentication tokens """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# Profile Feed ViewSet
class ProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles creating, Updating & Reading profile feed Items """
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = ( UpdateOwnStatus, IsAuthenticated)


    def perform_create(self, serializer):
        """ Sets user profile to the logged in user """
        serializer.save(user_profile=self.request.user)
