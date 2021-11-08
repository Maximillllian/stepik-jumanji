from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView

from .forms import SignUpForm


class UserLoginView(LoginView):
    template_name = 'authenticator/login.html'


class RegistrationView(CreateView):
    template_name = 'authenticator/registration.html'
    form_class = SignUpForm
    model = User
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        valid = super().form_valid(form)
        form.save()
        username = self.request.POST.get('username')
        password = self.request.POST.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return valid