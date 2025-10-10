from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Registration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect('login')  # make sure 'login' name exists in urls.py
        else:
            # Print errors to console (or use logger)
            print("Form errors:", fm.errors)
            messages.error(request, "Form is not valid. Please fix the errors below.")
    else:
        fm = Registration()

    # use key 'form' (conventional) — easier to use in template
    return render(request, 'register.html', {'forms': fm})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Email se user nikal lo
            user_obj = User.objects.get(email=email)
            # Fir authenticate username ke through
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request , user)
            return redirect('dashboard')
        else:
            print("❌ Login failed: Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')

def log_out(request):
        logout(request)
        return redirect('login')

def delete_task(request , id):
        return render(request , 'login.html')
       
       

