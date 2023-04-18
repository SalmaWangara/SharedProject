from django.urls import path, include
from . import views

# app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUp, name='signup'),
    path('login', views.login, name='login'),
]
