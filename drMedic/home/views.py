from django.shortcuts import render, redirect
from .form import SignupForm
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# from django.core.files.storage import FileSystemStorage
# Create your views here.


def home(request):
    return render(request, 'mediCare/index.html')
# def services(request):
#     return render(request, 'services.html')

def logIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                logIn(request, user)
                return redirect('home')
            else:
                return redirect('signup')
    else:
        form =AuthenticationForm()
    return render(request, 'mediCare/login.html', {'form':form})


def signUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signUp_user = User.objects.get(username = username)
            customer_group= Group.objects.get(name='Customer')
            customer_group.user_set.add(signUp_user)
    else:
        form = SignupForm()
    return render(request, 'mediCare/sign-up.html', {'form':form})



def customer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST('username')
            password = request.POST('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('customer_register')
    else:
        form = AuthenticationForm()
    return render(request, 'mediCare/login.html', {'form': form})
def logout(request):
    pass