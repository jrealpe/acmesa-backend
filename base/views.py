from django.contrib.auth import authenticate
from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        response = {'error': True,
                    'msg': 'Parámetros erroneos'}

        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(username=username, password=password)
        if user and user.is_superuser:
            token, created = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user, context={'token': token.key})

            response['data']  = serializer.data
            response['error'] = False
            response['msg']   = 'Inicio de sesión exitoso'
        else:
            response['msg'] = 'Usuario o Contraseña incorrectos'
        return Response(response)


login_view = LoginView.as_view()
