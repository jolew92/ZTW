from django.shortcuts import render
from movies.models import Movie, Person


def movie_list(request):
    movies = Movie.objects.order_by('title')
    return render(request, 'movie_list.html', {'movies': movies})


def people_list(request):
    people = Person.objects.order_by('last_name')
    return render(request, 'people_list.html', {'people': people})