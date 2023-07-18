from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
# Create your views here.

def index(request):
    return render(request, 'index.html')
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

@ensure_csrf_cookie
@csrf_protect
def login(request):
    if request.method == 'POST':
        # Process login form data and authenticate the user
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'user123' and password == 'password123':
            request.session['isLoggedIn'] = True
            request.session.set_expiry(30)  # Set session expiration to 10 minutes
            return redirect('dashboard')  # Replace 'apply' with your desired URL name
    return render(request, 'authentication/login.html')
def register(request):
    if request.method == 'POST':
            return redirect('dashboard')
    return render(request, 'authentication/register.html')

def logout(request):
    request.session.flush()
    return render(request, 'index.html')
def apply(request):
    return render(request, 'user_account/apply_form.html')
def dashboard(request):
    return render(request, 'user_account/dashboard.html')

