from django.urls import path
from .import views

urlpatterns = [
    path('login-user/', views.login, name= "login"),
    path('register-user/', views.register, name='register')
]