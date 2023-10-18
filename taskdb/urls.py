from django.contrib import admin
from django.urls import path,include
from taskdb import views

urlpatterns = [
    path('', views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('homepage/',views.homepage,name="homepage"),
    path('logout/',views.user_logout,name="logout"),
    path('accounts/', include('allauth.urls'),  name="accounts"),
    


]

