from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def hospitals(request):
    return render(request, 'mediCare/hospital.html')
class ServicesPageView(TemplateView):
    template_name = 'mediCare/service.html'
class ServiceCartPageView(TemplateView):
    template_name = 'mediCare/cart.html'
