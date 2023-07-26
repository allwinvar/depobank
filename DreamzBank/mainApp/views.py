from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    return render(request, 'index.html')
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie


@ensure_csrf_cookie
@csrf_protect
def login(request):
    if request.method == 'POST':
        # Process login form data
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'authentication/login.html', {'error': error_message})

        # Verify the password
        if password == user.password:
            # Passwords match, authenticate the user
            # Log in the user (if needed) using your desired logic

            # Example: Set a session variable to indicate the user is logged in
            request.session['user_id'] = get_random_string(length=32)
            request.session['isLoggedIn'] = True
            return redirect('dashboard')  # Replace 'dashboard' with your desired URL name

        error_message = "Invalid username or password. Please try again."
        return render(request, 'authentication/login.html', {'error': error_message})

    return render(request, 'authentication/login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            # Passwords do not match, handle the error as per your requirements
            error_message = "Passwords do not match. Please try again."
            return render(request, 'authentication/register.html', {'error': error_message})

        # Check if a user with the provided username already exists
        if User.objects.filter(username=username).exists():
            error_message = "Username already exists. Please choose a different username."
            return render(request, 'authentication/register.html', {'error': error_message})

        # Create a new User instance with the provided username and password
        user = User(username=username, password=password)

        # Save the user to the database
        user.save()

        return redirect('dashboard')

    return render(request, 'authentication/register.html')

def logout(request):
    request.session.flush()
    return render(request, 'index.html')
def apply(request):
    if request.method == 'POST':
        return render(request, 'user_account/success.html')
    return render(request, 'user_account/apply_form.html')
def dashboard(request):
    return render(request, 'user_account/dashboard.html')

