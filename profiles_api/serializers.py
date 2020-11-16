from rest_framework import serializers
from .models import UserProfile, ProfileFeedItem


class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing thr APIView """
    name = serializers.CharField(max_length=10)
    # email = serializers.EmailField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializes a user profile Object """

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        # set password to Read Only
        extra_kwargs = {
        'password' : {
            'write_only' : True,
            'style' : {'input_type' : 'password'}
            }
        }

    #  overwrite create_user function in Model of UserProfileManager
    def create(self, validated_data):
        """ Create and return a new user """

        user = UserProfile.objects.create_user(
        email = validated_data['email'],
        name = validated_data['name'],
        password = validated_data['password']
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ Serializes the profile feed item """

    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile' : { 'read_only' : True }}
