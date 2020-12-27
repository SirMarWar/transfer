from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from moneytransfer.decorators import unauthenticated_user, allowed_users
@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def dashboardPage(request):
    return render(request, 'dashboard/dashboard.html', {  })