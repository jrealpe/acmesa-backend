from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from . import viewsets


router = routers.DefaultRouter()
router.register(r'applications', viewsets.ApplicationViewSet)
router.register(r'roles', viewsets.RoleViewSet)
router.register(r'users', viewsets.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
