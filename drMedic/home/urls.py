from django.urls import path, include
from . import views

# app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signUp, name='signup'),
    path('login', views.customer_login, name='login'),
]
