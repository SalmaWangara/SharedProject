from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("User logged in successfully!")
                return redirect('home')
            else:
                print("Authentication failed: invalid username or password")
                return redirect('register')
        else:
            print("Form validation failed:", form.errors)
            return redirect('login')
    else:
        print("Form validation failed:", form.errors)
        form = AuthenticationForm()

def SignUp(request):
    if request.method == 'POST': ##if the requested method is post you call the sigupform
        form = SignupForm(request.POST)
        if form.is_valid():# here we check if the form is validated if yes save 
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)#the username we're getting from the input is store in the username(in the models)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)#if the group exists we create the user
            messages.info('success')
        print("Done")
        return redirect('login')
    else:
        form = SignupForm()
        print("Nope")
        return render(request, 'registration/sign-up.html', {'form':form})
        
def logout(request):
    pass