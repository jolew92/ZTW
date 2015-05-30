from django.template import RequestContext
from django.shortcuts import render
from movies.models import Movie
from people.models import Person
from django.views.generic import View
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils import translation


class HomeView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name, {'user': request.user}, context_instance=RequestContext(request))


class SearchView(View):
    template_all = 'search/searchAll.html'
    template_movie = 'search/searchMovie.html'
    template_person = 'search/searchPerson.html'

    def get(self, request):
        language = translation.get_language_from_request(request)
        what = request.GET['what_to_search']
        search = request.GET['search']
        if search == '':
            return HttpResponseRedirect('/')
        else:
            if what == 'all':
                movies = Movie.objects.filter(Q(title__icontains=search) | Q(title_en__icontains=search))
                people = Person.objects.all()
                for term in search.split():
                    people = people.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
                return render(request, self.template_all, {'movies': movies, 'people': people, 'search': search})
            elif what == 'movie':
                movies = Movie.objects.filter(Q(title__icontains=search) | Q(title_en__icontains=search))
                return render(request, self.template_movie, {'movies': movies, 'search': search})
            elif what == 'person':
                people = Person.objects.all()
                for term in search.split():
                    people = people.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
                return render(request, self.template_person, {'people': people, 'search': search})