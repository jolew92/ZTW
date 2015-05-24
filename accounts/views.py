from django.shortcuts import render_to_response, render, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from accounts.forms import RegistrationForm, UpdateProfile
from django.views.generic import View
from django.contrib.auth.models import User
from list.models import MovieList, MovieListItem
from django.utils import translation
from movies.models import Movie


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


class EditListsView(View):
    template_name = 'edit_lists.html'

    def get(self, request):
        if request.user.is_authenticated():
            lists = MovieListItem.objects.filter(movielist__user=request.user)
            return render(request, self.template_name, {'lists': lists, 'user': request.user})
        else:
            return HttpResponseRedirect('/')


class EditListView(View):
    template_name = 'edit_list.html'

    def get(self, request, movielistitem_id=1):
        if request.user.is_authenticated():
            list = MovieListItem.objects.get(id=movielistitem_id)
            return render(request, self.template_name, {'list': list})
        else:
            return HttpResponseRedirect('/')


def remove_list(request):
    language = translation.get_language_from_request(request)
    if request.user.is_authenticated():
        list_id = request.GET['list']
        MovieListItem.objects.filter(id=list_id).delete()
        return HttpResponseRedirect(redirect_to='/'+language+'/accounts/edit_list/')
    else:
        return HttpResponseRedirect('/')


def add_list(request):
    language = translation.get_language_from_request(request)
    if request.user.is_authenticated():
        list_name = request.POST.get('list_name', '')
        if MovieList.objects.filter(user=request.user).exists():
            movie_list = MovieList.objects.get(user=request.user)
        else:
            movie_list = MovieList.objects.create(user=request.user)
        list = MovieListItem.objects.create(name=list_name, movielist=movie_list)
        list.save()
        return HttpResponseRedirect(redirect_to='/'+language+'/accounts/edit_list/')
    else:
        return HttpResponseRedirect('/')


def change_list_name(request, list_id):
    language = translation.get_language_from_request(request)
    if request.user.is_authenticated():
        list_name = request.POST.get('list_name', '')
        list = MovieListItem.objects.get(id=list_id)
        list.name = list_name
        list.save()
        return HttpResponseRedirect(redirect_to='/'+language+'/accounts/edit_list/'+list_id+'/')
    else:
        return HttpResponseRedirect('/')


def remove_movie(request, list_id):
    language = translation.get_language_from_request(request)
    if request.user.is_authenticated():
        movie_id = request.GET['movie']
        MovieListItem.movies.through.objects.get(movielistitem__id=list_id, movie__id=movie_id).delete()
        return HttpResponseRedirect(redirect_to='/'+language+'/accounts/edit_list/'+list_id+'/')
    else:
        return HttpResponseRedirect('/')