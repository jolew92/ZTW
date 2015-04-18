from django.shortcuts import render
from movies.models import Movie
from people.models import Person
from django.views.generic import View
from django.db.models import Q
from django.http import HttpResponseRedirect


class SearchView(View):
    template_name = 'search.html'

    def get(self, request):
        search = request.GET['search']
        if search == '':
            return HttpResponseRedirect('/')
        else:
            movies = Movie.objects.filter(title__icontains=search)
            people = Person.objects.all()
            for term in search.split():
                people = people.filter(Q(first_name__icontains=term) | Q(last_name__icontains=term))
            return render(request, self.template_name, {'movies': movies, 'people': people, 'search': search})