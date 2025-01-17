from django.shortcuts import render, redirect
from app.forms import AccountAuthenticationForm, SignupForm
from app.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('index')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                messages.success(request, 'Logged in Sucessfully!!')
                return redirect("index")
    else:
        form = AccountAuthenticationForm()
    return render(request, 'registration/login.html', {'login_form':form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out Sucessfully!!')
    return redirect("index")

def signup_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('index')
    
    context = {}
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            url = request.META.get('HTTP_REFERER')
            messages.success(request, 'Account created successfully!')
            return redirect(url)
        else:
            context['signup_form'] = form
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html',  {'signup_form':form})

def about_us_view(request):
    return render(request, 'app/about.html')

def profile(request):
    user = request.user
    if user.is_authenticated:
        user_id = user.id
        user = User.objects.get(pk=user_id)
        f_name = user.name.split()[0]
        date_obj = datetime.fromisoformat(str(user.date_joined))
        formatted_date = date_obj.strftime("%B %d, %Y")
    else:
        return redirect('login')

    return render(request, 'app/profile.html', {'first_name':f_name, "user":user, "date_joined":formatted_date})