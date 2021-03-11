from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *


# Create your views here.
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user= form.save()
            profileObject = Profile(
                user = user
            )
            profileObject.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Your now able to login')
            return redirect('accounts:login')

    context = {
        'form':form,
    }
    return render(request, 'authentication/registration.html', context)
