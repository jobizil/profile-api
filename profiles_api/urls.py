from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HelloApiView, HelloViewSet, UserProfileViewSet


# router = routers.DefaultRouter()
router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, 'viewset' )
router.register('profile', UserProfileViewSet)


urlpatterns = [
path('hello-views/', HelloApiView.as_view()),
path('', include(router.urls))
]
