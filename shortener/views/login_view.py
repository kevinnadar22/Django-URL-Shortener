from pyexpat.errors import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib import messages


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            messages.success(request, 'Logged in Successfully')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credits')


    return render(request, 'shortener/login.html')