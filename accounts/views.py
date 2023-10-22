from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django_htmx.http import HttpResponseClientRedirect
from django.urls import reverse

User = get_user_model()

# Create your views here.
def login_user(request):
    ctx = {'title': 'Login'}
    return render(request, 'accounts/login.html', ctx)

def register(request):
    ctx = {'title': 'Register'}
    return render(request, 'accounts/register.html', ctx)

def logout_user(request):
    logout(request)
    return redirect(reverse('login'))

def htmx_login(request):
    status = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"testing >>> : {username} {password}")
        if len(username) == 0:
            status = "Username is required"
        elif len(password) == 0:
            status = "Password is required"
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseClientRedirect('/')  # redirect
            else:
                status = "Invalid username or password"
    ctx = {'status': status}
    return render(request, 'partials/login_form.html', ctx)

def htmx_register(request):
    status = ""
    if request.method == 'POST':
        # extraction
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')
        print(f"testing >>> : {username} {password} {cpassword} {email}")
        # validation
        # todo
        # processing
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save() # save to db
        # response
        status = "Register successful"
        return HttpResponseClientRedirect('/') # redirect
    ctx = {'status': status}
    return render(request, 'partials/register_form.html', ctx)