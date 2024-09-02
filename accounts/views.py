from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import userForm
from vendor.forms import VendorForm
# httpresp
from django.http import HttpResponse as HTTPResponse

# Create your views here.

def registerUser(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    elif request.method == "POST":
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


def login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    elif request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.get(email=email)
        
        if user.check_password(password):
            if user.role == User.CUSTOMER:
                return redirect("custDashboard")
            elif user.role == User.VENDOR:
                return redirect("vendorDashboard")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")
    return render(request, "accounts/login.html")

def logout(request):
    return redirect("login")

def vendorDashboard(request):
    return render(request,"accounts/vendorDashboard.html")

def custDashboard(request):
    return render(request,"accounts/custDashboard.html")

def dashboard(request):
    return render(request, "accounts/dashboard.html")