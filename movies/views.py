from django.shortcuts import render
from movies.models import Movie


def movie_list(request):
    movies = Movie.objects.order_by('title')
    return render(request, 'movie_list.html', {'movies': movies})