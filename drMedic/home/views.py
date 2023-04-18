from django.shortcuts import render, redirect
from .form import SignupForm
from django.contrib import messages
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

# def logIn(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data= request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 logIn(request, user)
#                 return redirect('home')
#             else:
#                 return redirect('signup')
#     else:
#         form =AuthenticationForm()
#     return render(request, 'mediCare/login.html', {'form':form})

def SignUp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['lasst_name']
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        if password == confirm_password:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Username Already Exists')
                return redirect(SignUp)
            else:
                new_user = User.objects.create_user(username=email, password=password, first_name=first_name, last_name=last_name)
                new_user.set_password(password)
                new_user.save()
                print("Success!!!!")
                return redirect(login)
    else:
        print("This is not a post method")
        return redirect('signup')
def login(request):
    return render(request, 'mediCare/login.html')
# def signUp(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             signUp_user = User.objects.get(username = username)
#             customer_group= Group.objects.get(name='Customer')
#             customer_group.user_set.add(signUp_user)
#     else:
#         form = SignupForm()
#     return render(request, 'mediCare/sign-up.html', {'form':form})



# def customer_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST('username')
#             password = request.POST('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 return redirect('customer_register')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'mediCare/login.html', {'form': form})
# def logout(request):
#     pass