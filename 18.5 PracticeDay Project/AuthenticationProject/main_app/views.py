from django.shortcuts import render,redirect
from .forms import registerForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'home.html')

def User_register(request):
    # if not request.user.is_authenicated:
        if request.method == 'POST':
            form = registerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account created successfully')
        else:
            form = registerForm()
        return render(request,'registerAndLogin.html',{'form': form,'type':'Register'})
    # else:
        # return redirect('profile')

def User_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name,password =user_pass)
            if user is not None:
                login(request,user)
                messages.success(request, 'Logged in successfully')
                return redirect('profile')
            else:
                messages.warning(request,'Your enterd information is incorrect')
                return redirect('login')
    else:
        form = AuthenticationForm(request, request.POST)
        return render(request, 'registerAndLogin.html',{'form':form, 'type':'Login'})
    
@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def PassWord_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password_change.html', {'form' : form})

@login_required
def PassWord_change2(request):
       if request.method == 'POST':
            form = SetPasswordForm(user= request.user, data = request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Password Updated Successfully')
                update_session_auth_hash(request, request.user)
                return redirect('profile')
       else:
            form = SetPasswordForm(user= request.user)
       return render(request, './password_change.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Log Out Successfully')

    return redirect('login')
