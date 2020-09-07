from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import RegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            # username = form.cleaned_data('username')
            # messages.success(request, f'Account Created For {username}')
            return redirect('homePath')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})
