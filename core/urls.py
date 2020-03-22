from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'results', views.MediaViewset, basename='media')
urlpatterns = [
    path('', include(router.urls)),
]
