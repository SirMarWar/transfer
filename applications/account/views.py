from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data['email']
                messages.success(request, f'Account was created for {email}')
                return redirect('login')

        return render(request, 'account/register.html', {'form': form})


def loginPage(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home')
    else:
            
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            #regex = re.compile('^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$', re.I)
            #match = regex.match(email_user)
            #if(bool(match)):
                #user = authenticate(request, email=email_user, password=password)
            #else:
            #user = authenticate(request, username=User.objects.get(email=email).username, password=password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, "email or password is incorrect")
        return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def resetpassword(request):
    return HttpResponse("reset")