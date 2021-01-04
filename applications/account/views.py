from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreateUserForm
from .models import Profile, State
from moneytransfer.decorators import unauthenticated_user, allowed_users


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name="customer")
            user.groups.add(group)

            Profile.objects.create(user=user, state=State.objects.get(code="CTMA"))

            email = form.cleaned_data["email"]
            messages.success(request, f"Account was created for {email}")
            return redirect("login")

    return render(request, "account/register.html", {"form": form})


@unauthenticated_user
def loginPage(request):
    context = {}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # regex = re.compile('^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$', re.I)
        # match = regex.match(email_user)
        # if(bool(match)):
        # user = authenticate(request, email=email_user, password=password)
        # else:
        # user = authenticate(request, username=User.objects.get(email=email).username, password=password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            messages.info(request, "email or password is incorrect")
    return render(request, "account/login.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["customer"])
def userPage(request):
    orders = request.user.customer.order_set.all()
    print("ORDERS", oeders)

    context = {orders: orders}
    return render(request, "accounts/user.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


def resetpassword(request):
    return HttpResponse("reset")


def profileinfo(request):
    context = {}
    return render(request, "profile/info.html", context)


def profilenotifications(request):
    context = {}
    return render(request, "profile/notification.html", context)


def profilebank(request):
    context = {}
    return render(request, "profile/bankaccount.html", context)
