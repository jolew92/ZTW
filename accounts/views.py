from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from accounts.forms import RegistrationForm
from django.views.generic import View


class LoginView(View):
    def get(self, request):
        c = {}
        c.update(csrf(request))
        return render_to_response('login.html', c)


class AuthView(View):
    def get(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/accounts/loggedin')
        else:
            return HttpResponseRedirect('/accounts/invalid')


class LoggedinView(View):
    def get(self, request):
        return render_to_response('loggedin.html',
                              {'user': request.user})


class InvalidLoginView(View):
    def get(self, request):
        return render_to_response('invalid_login.html')


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return render_to_response('logout.html')


class RegisterUserView(View):
    def get(self, request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/accounts/register_success')

        args = {}
        args.update(csrf(request))

        args['form'] = RegistrationForm()
        return render_to_response('register.html', args)


class RegisterSuccessrView(View):
    def get(self, request):
        return render_to_response('register_success.html')