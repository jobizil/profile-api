from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import HelloApiView, HelloViewSet


# router = routers.DefaultRouter()
router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, 'viewset' )


urlpatterns = [
path('hello-views/', HelloApiView.as_view()),
path('', include(router.urls))
]
