from django.shortcuts import render, redirect

# Create your views here.

def dashboardPage(request):
    return render(request, 'dashboard/dashboard.html', {  })