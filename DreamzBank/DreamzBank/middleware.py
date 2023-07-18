from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        isLoggedIn = request.session.get('isLoggedIn', False)
        if not isLoggedIn and request.path.startswith('/account/'):
            return redirect('login')  # Replace 'login' with your actual login URL name
        response = self.get_response(request)
        return response
