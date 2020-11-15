from django.urls import path
from . import views
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register('cars', views.CarViewSet, basename='cars')

urlpatterns = [
    path('version', views.GetAppVersion.as_view()),
] + router.urls

