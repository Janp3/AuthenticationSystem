from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def login_template(request):
    if request.method == 'GET':
        return render(request, 'login/pages/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return render(request, 'login/pages/index.html')
        messages.error(request, 'User/password is invalid or does not exist')
        return render(request, 'login/pages/login.html')


def logout_template(request):
    logout(request)
    return login_template(request)


def register_template(request):
    if request.method == 'GET':
        return render(request, 'login/pages/register.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        user = User.objects.filter(username=username).first()
        password_bool = password != re_password
        is_empty = (username == '' or email == ''
                    or password == '' or re_password == '')
        if user:
            messages.error(request, 'User already exist')
            return render(request, 'login/pages/register.html')
        elif password_bool:
            messages.warning(request, 'Passwords are not equal')
            return render(request, 'login/pages/register.html')
        elif is_empty:
            messages.warning(request, 'Fulfill all the informations')
            return render(request, 'login/pages/register.html')
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Registration complete sucessfuly')
        return render(request, 'login/pages/register.html')


def index(request):
    return render(request, 'login/pages/index.html')


@login_required(login_url='system:login')
def home(request):
    return render(request, 'login/pages/home.html')
