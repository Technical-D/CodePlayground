from django.shortcuts import render, redirect
from app.forms import AccountAuthenticationForm, SignupForm
from app.models import User, Problem, UserProblem
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from datetime import datetime
import subprocess
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

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

@login_required
def profile(request):
    user = request.user
    user_id = user.id
    user = User.objects.get(pk=user_id)
    f_name = user.name.split()[0]
    date_obj = datetime.fromisoformat(str(user.date_joined))
    formatted_date = date_obj.strftime("%B %d, %Y")

    return render(request, 'app/profile.html', {'first_name':f_name, "user":user, "date_joined":formatted_date})

def python_interpreter_view(request):
    user = request.user
    if not user.is_authenticated:
        messages.warning(request, "Please login before accessing interpreter!")
        return redirect('login')

    return render(request, 'app/interpreter.html')

@login_required
@csrf_exempt 
def run_python(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            code = data.get("code", "")
            
            output = subprocess.run(['python', '-c', code], capture_output=True, text=True, timeout=5)
            print(output.stdout, output.stderr)
            return JsonResponse({'output': output.stdout, 'error': output.stderr})
        except subprocess.TimeoutExpired:
            return JsonResponse({'error': 'Error: Code execution timed out. Please check your code for infinite loops or inefficiencies.'})
        except Exception as e:
            return JsonResponse({'error': f"Error: {str(e)}"})
    else:
        return JsonResponse({'error': 'Invalid method, POST required.'}, status=405)

@login_required
def problems_view(request):
    problems = Problem.objects.all()
    solved_problems = set(UserProblem.objects.filter(user=request.user, solved=True).values_list('problem_id', flat=True))

    return render(request, 'app/problems.html', {'problems':problems, 'solved_problems': solved_problems})