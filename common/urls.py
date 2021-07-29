from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.check.as_view(), name='check'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.login.as_view(), name='login'),
    path('logout/', views.logout.as_view(), name='logout')
]
