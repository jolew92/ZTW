from django.shortcuts import render_to_response
from movies.models import Movie, Description, Role, MovieRole


def movies(request):
    movies = Movie.objects.order_by('title')
    return render_to_response('movies.html', {'movies': movies})


def movie(request, movie_id=1):
    desc = Description.objects.filter(movie_id=movie_id)
    movie_roles = MovieRole.objects.filter(movie_id=movie_id)
    return render_to_response('movie.html', {'movie': Movie.objects.get(id=movie_id), 'desc': desc,
                                             'roles': Role.objects, 'movie_roles': movie_roles})


