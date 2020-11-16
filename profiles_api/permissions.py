from rest_framework.permissions import BasePermission, SAFE_METHODS

class UpdateOwnProfile(BasePermission):
    """ Allows user to edit personal profile """

    # Returns a True or False to determine authentication of user
    def has_object_permission(self, request, view, obj):
        """ Check User Profile for permission """
        #  Safe Methods are methods that do not require or make changes to an object eg GET requests
        if request.method in SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(BasePermission):
    """ Allows user to update personal status"""

    def has_object_permission(self, request, view, obj):
        """ Checks if user is trying to update their own status """
        if request.method in SAFE_METHODS:
            return True
        return obj.id == request.user.id
