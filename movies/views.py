from django.shortcuts import render
from movies.models import Movie, Description, Role, MovieRole
from django.views.generic import View


class MoviesView(View):
    template_name = 'movies.html'

    def get(self, request):
        movies = Movie.objects.order_by('title')
        return render(request, self.template_name, {'movies': movies})


class MovieView(View):
    template_name = 'movie.html'

    def get(self, request, movie_id=1):
        desc = Description.objects.filter(movie_id=movie_id)
        movie_roles = MovieRole.objects.filter(movie_id=movie_id)
        return render(request, self.template_name, {'movie': Movie.objects.get(id=movie_id),
                                                    'desc': desc, 'roles': Role.objects, 'movie_roles': movie_roles})



