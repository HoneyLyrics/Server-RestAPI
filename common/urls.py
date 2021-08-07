from django.urls import path
from . import views

urlpatterns = [
    #path('check', views.Check.as_view(), name='check'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    #path('login/refresh'),
    #path('logout', views.Logout.as_view(), name='logout')
]
