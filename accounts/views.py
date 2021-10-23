from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import LoginForm, RegisterForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class UserLogin(LoginView):
    template_name = 'registration/login.html'
    authentication_form = LoginForm

    def form_valid(self, form):
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        login(self.request, user)
        return render(self.request, 'registration/profile.html')


class UserRegisterView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


def logout_view(request):
    auth.logout(request)
    return redirect('login')


@login_required
def show_person_cabinet(request):
    return render(request, 'registration/profile.html')

