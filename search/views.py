from django.shortcuts import render
from movies.models import Movie
from people.models import Person
from django.views.generic import View
from django.db.models import Q
from django.http import HttpResponseRedirect


class SearchView(View):
    template_all = 'searchAll.html'
    template_movie = 'searchMovie.html'
    template_person = 'searchPerson.html'

    def get(self, request):
        what = request.GET['what_to_search']
        search = request.GET['search']
        if search == '':
            return HttpResponseRedirect('/')
        else:
            if what == 'all':
                movies = Movie.objects.filter(title__icontains=search)
                people = Person.objects.all()
                for term in search.split():
                    people = people.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
                return render(request, self.template_all, {'movies': movies, 'people': people, 'search': search})
            elif what == 'movie':
                movies = Movie.objects.filter(title__icontains=search)
                return render(request, self.template_movie, {'movies': movies, 'search': search})
            elif what == 'person':
                people = Person.objects.all()
                for term in search.split():
                    people = people.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
                return render(request, self.template_person, {'people': people, 'search': search})