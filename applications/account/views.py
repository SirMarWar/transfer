from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from  .forms import CreateUserForm

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            messages.success(request, f'Account was created for {email}')
            return redirect('login')
    
    return render(request, 'account/register.html', { 'form': form })

def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, username)
            redirect('home')
    return render(request, 'account/login.html', context)