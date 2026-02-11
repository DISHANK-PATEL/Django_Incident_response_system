from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResponderTeamViewSet

router = DefaultRouter()

router.register(r'teams', ResponderTeamViewSet, basename='responder-teams')

urlpatterns = [
    path('', include(router.urls)),
]