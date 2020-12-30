from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("resetpassword/", views.resetpassword, name="resetpassword"),
    path("profileinfo/", views.profileinfo, name="profileinfo"),
    path("profilebank/", views.profilebank, name="profilebank"),
    path(
        "profilenotifications/", views.profilenotifications, name="profilenotifications"
    ),
]
