from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "settingapp/index.html")
