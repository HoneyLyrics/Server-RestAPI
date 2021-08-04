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
    

class Login(View):
    """
    """
    pass

class Logout(View):
    """
    """
    pass

class Check(View):
    """
    """
    pass