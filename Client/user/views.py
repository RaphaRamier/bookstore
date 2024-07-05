from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from Client.user.forms import LoginForm


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form=LoginForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'{request.user.username} successfully logged in')
                    return redirect('home')
                else:
                    form.add_error(None, 'Invalid username or password')
                    messages.error(request, 'Invalid username or password')
        else:
            form=LoginForm()

    return render(request, 'user/login.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout')
    return redirect('login')
