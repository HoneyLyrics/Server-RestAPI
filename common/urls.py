from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.Check.as_view(), name='check'),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout')
]
