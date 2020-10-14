from django.shortcuts import render

# Create your views here.

def dashboardPage(request):
    form = CreateUserForm()
    return render(request, 'dashboard/dashboard.html', { 'form': form })