from django.shortcuts import render,redirect
from . import forms
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import models
# This Class based muscian add CreateView 
@method_decorator(login_required, name= 'dispatch')
class AddMusician(CreateView):
    model = models.musician_model
    form_class = forms.MusicainForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')

    def form_valid(self, form):
        form.instance.musician = self.request.user
        return super().form_valid(form)


# This Class based user registation form 
class SignUpViewClass(SuccessMessageMixin, CreateView):
     template_name = 'form.html'
     success_url = reverse_lazy('register')
     form_class = forms.RegistationForm
     success_message = "Your account was created successfully "

     def form_valid(self,form):
          response = super().form_valid(form)
          messages.success(self.request, self.success_message)
          return response
     def get_context_data(self,**kwargs):
         context = super().get_context_data(**kwargs)
         context['type'] = 'Register'
         return context

# This Class based user Login  

class UserLoginViewClass(LoginView):
    template_name = 'form.html'
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        messages.success(self.request, 'You are successfully logged in')
        # form
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Your provided information is incorrect')
        # form
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

# This Class based user Logout
@method_decorator(login_required, name= 'dispatch')
class UserLogoutViewClass(LogoutView):
    template_name = 'logout.html'
    def get_success_url(self):
       return reverse_lazy('homepage')
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        messages.success(self.request, "You have been successfully logged out.")
        return response