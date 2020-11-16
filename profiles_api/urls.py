from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HelloApiView, HelloViewSet, UserProfileViewSet, UserLoginApiView, ProfileFeedViewSet


# router = routers.DefaultRouter()
router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, 'viewset' )
router.register('profile', UserProfileViewSet)
router.register('feed', ProfileFeedViewSet)



urlpatterns = [
path('hello-views/', HelloApiView.as_view()),
path('login/', UserLoginApiView.as_view()),
path('', include(router.urls))
]
