from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import userForm
from vendor.forms import VendorForm

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

def registerVendor(request):
    if request.method == "POST":
        form = userForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        print("form valid", form.is_valid())
        print("v_form valid", v_form.is_valid())
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            vendor.user_profile = user.userprofile
            vendor.save()
            
            return redirect("registerVendor")
    else:
        form = userForm()
        v_form = VendorForm()
    context = {
        "form": form,
        "v_form": v_form
    }
    return render(request, "accounts/registerVendor.html", context)

