from django.shortcuts import render_to_response, render, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from accounts.forms import RegistrationForm, UpdateProfile
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class EditView(View):
    template_name = 'edit.html'

    def get(self, request):
        if request.user.is_authenticated():
            return render(request, self.template_name)
        else:
            return HttpResponseRedirect('/')


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        c = {}
        c.update(csrf(request))
        return render(request, self.template_name, c)


class LoggedinView(View):
    template_name = 'loggedin.html'

    def get(self, request):
        return render(request, self.template_name, {'user': request.user})


class InvalidLoginView(View):
    template_name = 'invalid_login.html'

    def get(self, request):
        return render(request, self.template_name)


class LogoutView(View):
    template_name = 'logout.html'

    def get(self, request):
        auth.logout(request)
        return render(request, self.template_name)


class RegisterSuccess(View):
    template_name = 'register_success.html'

    def get(self, request):
        return render(request, self.template_name)


def update_profile(request):
    args = {}
    if request.method == 'POST':
        user_instance = User.objects.get(id=request.user.id)
        form = UpdateProfile(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/edit_user/')
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'edit_user.html', args)


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success/')

    args = {}
    args.update(csrf(request))

    args['form'] = RegistrationForm()
    return render_to_response('register.html', args)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')