from django.shortcuts import render
from movies.models import Movie, Description, Role, MovieRole, Rate
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils import translation

class MoviesView(View):
    template_name = 'movies.html'

    def get(self, request):
        movies = Movie.objects.order_by('title')
        return render(request, self.template_name, {'movies': movies})


class MovieView(View):
    template_name = 'movie.html'

    def get(self, request, movie_id=1):
        ocena = Rate.objects.filter(movie_id=movie_id, user_id=request.user.id)
        desc = Description.objects.filter(movie_id=movie_id)
        movie_roles = MovieRole.objects.filter(movie_id=movie_id)
        if len(ocena) != 0 :
            return render(request, self.template_name, {'movie': Movie.objects.get(id=movie_id),
                                                    'desc': desc, 'roles': Role.objects, 'movie_roles': movie_roles, 'ocena':ocena[0].rate})
        else:
            return render(request, self.template_name, {'movie': Movie.objects.get(id=movie_id),
                                                    'desc': desc, 'roles': Role.objects, 'movie_roles': movie_roles})


def set_rating(request, movie_id=1):
    language = translation.get_language_from_request(request)
    #filmid = request.GET['movie_id']
    ocena = request.GET['ocena']
#        ocena = int(request.GET.get('rating'))
    u = request.user.id
    oceny = Rate.objects.filter(movie_id=movie_id, user_id=request.user.id)
    if len(oceny) == 0 :
        r=Rate(rate=ocena,user = User.objects.get(id=u), movie = Movie.objects.get(id = movie_id))
        r.save()
    else:
        oceny[0].rate = ocena
        oceny[0].save()
    return HttpResponseRedirect(redirect_to='/'+language+'/movies/get/'+movie_id)
    #return HttpResponse(template_name = 'movie.html')
