from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import userForm

# Create your views here.

def registerUser(request):
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.role=User.CUSTOMER
            form.save()
            messages.success(request, "User registered successfully")
            return redirect("registerUser")
    else:
        form = userForm()
    context = {
        "form": form
    }
    return render(request, "accounts/registerUser.html", context)

def registerRestaurent(request):
    return render(request, "accounts/registerRestaurent.html")
