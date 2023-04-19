from django.urls import path, include
from . import views

# app_name = 'home'
urlpatterns = [
    path('', views.login, name='accounts'),
    path('signup/', views.SignUp, name='signup'),
]
