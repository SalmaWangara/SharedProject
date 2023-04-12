from django.urls import path
from . import views
from .views import ServicesPageView, ServiceCartPageView


urlpatterns = [
    path('', views.hospitals, name='hospitals'),
    path('contact/', ServicesPageView.as_view(), name='services'),
    path('cart/', ServiceCartPageView.as_view(), name='cart')
]
