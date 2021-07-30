from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from django.http.response import HttpResponse
from django.db.models import Q
from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
class Register(View):
    """ Create Register by Post method
        returns:
            HTTP Response
    """
    pass

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