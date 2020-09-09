""""""

# Import django libraries
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout


def logout(request):
    """
    Function is a view for logout
    :param request:
    :return:
    """
    do_logout(request)
    return redirect('/login/')


def login(request):
    """
    Function is a view login.
    :param request:
    :return:
    """
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                messages.success(request, "Bienvenido {}".format(user.username))
                if request.GET.get("next"):
                    return HttpResponseRedirect(request.GET["next"])
                return redirect('main:list-scheduler')
    return render(request, "main/login.html", {'form': form})
