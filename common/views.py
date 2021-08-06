from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from django.http.response import HttpResponse, ResponseHeaders
from django.db.models import Q
from .serializers import UserSerializer, UserSerializerWithToken, RegisterSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from django.contrib import auth
from django.conf import settings
import json
import jwt




# Create your views here.
class RegisterView(GenericAPIView):
    """ Create Register by Post method
        returns:
            HTTP Response
    """
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save() 
                return Response({'username':serializer.data['username']}, status=status.HTTP_200_OK)
            return Response({'error':'already exists'}, status=status.HTTP_409_CONFLICT)
        except Exception as e:
            return Response({'error':e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 

class LoginView(GenericAPIView):
    """ Login by Post method
        returns:
            HTTP Response
    """
    def post(self, request):
        try:
            data = request.data
            username = data.get('username','')
            password = data.get('password','')
            user = auth.authenticate(username=username, password=password)
            if user:
                # TODO change SECRET KEY
                auth_token = jwt.encode(
                    {'username': username}, settings.SECRET_KEY, algorithm="HS256")
                serializers = UserSerializer(user)
                data = {'username': serializers.data.get('username')}
                response = Response(data, status=status.HTTP_200_OK)
                response.set_cookie('access_token',auth_token)
                return response
            return Response({'username': username, 'error': 'wrong password'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            data = json.dumps({'error': str(e)}, ensure_ascii=False).encode('utf-8')
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Logout(View):
    """
    """
    pass

class Check(View):
    """
    """
    pass