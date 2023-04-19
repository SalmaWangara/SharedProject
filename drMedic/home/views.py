from django.shortcuts import render, redirect


# from django.core.files.storage import FileSystemStorage
# Create your views here.


def home(request):
    return render(request, 'mediCare/index.html')
