from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import ClientRegisterForm
from .decorators import unauthenticated


@unauthenticated
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        # else:
        #     messages.info('Invalid username or password')

    context = {}
    return render(request, 'users/login.html', context)


@unauthenticated
def registerPage(request):
    form = ClientRegisterForm()
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created')
            return redirect('login')
        # else:
        #     error = form.errors
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required(login_url='/login')
def dashboardPage(request):
    return render(request, 'users/dashboard.html')


@login_required(login_url='/login')
def profilePage(request):
    return render(request, 'users/profile.html')


@login_required(login_url='/login')
def investPage(request):
    return render(request, 'users/invest.html')


@login_required(login_url='/login')
def investment_historyPage(request):
    return render(request, 'users/investment_history.html')


@login_required(login_url='/login')
def depositPage(request):
    return render(request, 'users/deposit_history.html')


@login_required(login_url='/login')
def deposit_historyPage(request):
    return render(request, 'users/deposit_history.html')


@login_required(login_url='/login')
def withdrawPage(request):
    return render(request, 'users/withdraw.html')


@login_required(login_url='/login')
def withdrawal_historyPage(request):
    return render(request, 'users/withdrawal_history.html')


@login_required(login_url='/login')
def affiliatePage(request):
    return render(request, 'users/affiliate.html')


def logoutPage(request):
    logout(request)
    return redirect('login')
