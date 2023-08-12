from django.urls import path, include
from django.urls import path
from rest_framework import routers

from api import views
from api.views import MovieViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
