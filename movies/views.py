from django.shortcuts import render_to_response
from movies.models import Movie


def movies(request):
    movies = Movie.objects.order_by('title')
    return render_to_response('movies.html', {'movies': movies})


def movie(request, movie_id=1):
    return render_to_response('movie.html', {'movie': Movie.objects.get(id=movie_id)})


