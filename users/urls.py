from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('dashboard', views.dashboardPage, name='dashboard'),
    path('deposit', views.depositPage, name='deposit'),
    path('deposit_history', views.deposit_historyPage, name='deposit_history'),
    path('withdraw', views.withdrawPage, name='withdraw'),
    path('withdrawal_history', views.withdrawal_historyPage,
         name='withdrawal_history'),
    path('invest', views.investPage, name='invest'),
    path('investment_history', views.investment_historyPage,
         name='investment_history'),
    path('profile', views.profilePage, name='profile'),
    path('affiliate', views.affiliatePage, name='affiliate'),
    path('logout', views.logoutPage, name='logout'),



]
