from django.contrib import admin
from django.urls import path, include

from . import views, viewsets


urlpatterns = [
    path('login/', views.login_view)
]
