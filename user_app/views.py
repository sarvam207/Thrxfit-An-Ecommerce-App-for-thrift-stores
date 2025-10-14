from django.shortcuts import render
from django.shortcuts import redirect

from . forms import CreateUserForm, LoginForm
from django.contrib import messages


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.



def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('store_app')

    return render(request, 'user_app/registration/register.html', {'form': form})



def user_login(request):
    form = LoginForm()
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            
            if user is not None:
                auth.login(request, user)
                
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
           
                return redirect('user_login')
            
    return render(request, 'user_app/login/login.html', {'form': form})


def user_logout(request):
    
    auth.logout(request)
    return redirect('store_app')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'user_app/dashboard.html')