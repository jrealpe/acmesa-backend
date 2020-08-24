from django.contrib.auth.models import User

from rest_framework import viewsets

from .models import Application, Role, Permission
from .serializers import (
    ApplicationSerializer,
    RoleSerializer,
    PermissionSerializer,
    UserSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
