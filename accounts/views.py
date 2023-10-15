from django.shortcuts import render

# Create your views here.
def login(request):
    ctx = {}
    return render(request, 'accounts/login.html', ctx)

def register(request):
    ctx = {}
    return render(request, 'accounts/register.html', ctx)

def htmx_login(request):
    ctx = {}
    return render(request, 'partials/login_form.html', ctx)

def htmx_register(request):
    ctx = {}
    return render(request, 'partials/register_form.html', ctx)