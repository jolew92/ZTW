from django.shortcuts import render
from movies.models import Movie, Description, Role, MovieRole, Rate, Avg,RoleRate, AvgRole
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils import translation
import django.core.exceptions

class MoviesView(View):
    template_name = 'movies.html'

    def get(self, request):
        movies = Movie.objects.order_by('title')
        return render(request, self.template_name, {'movies': movies})


class MovieView(View):
    template_name = 'movie.html'

    def get(self, request, movie_id=1):
        ocena = Rate.objects.filter(movie_id=movie_id, user_id=request.user.id)
        #oceny = RoleRate.objects.filter(role_id=role_id, user_id=request.user.id)

        try:
            avg = Avg.objects.get(movie=Movie.objects.get(id=movie_id))
            srednia = avg.sumVotes/float(avg.numberOfVotes)
            test=1
        except Avg.DoesNotExist:
            srednia = 0
            test=0

        desc = Description.objects.filter(movie_id=movie_id)
        movie_roles = MovieRole.objects.filter(movie_id=movie_id)

        roles = MovieRole.objects.filter(movie_id=movie_id)
        przekazujeoceny = RoleRate.objects.filter(user_id=request.user.id, role__in=roles)


        if len(ocena) != 0:

            return render(request, self.template_name, {'movie': Movie.objects.get(id=movie_id),
                                                    'desc': desc, 'roles': Role.objects, 'movie_roles': movie_roles, 'ocena':ocena[0].rate,
                                                    'srednia':srednia,'ocenaR':przekazujeoceny})
        elif len(ocena) == 0 and test == 1:
            return render(request, self.template_name, {'movie': Movie.objects.get(id=movie_id),
                                                    'desc': desc, 'roles': Role.objects, 'movie_roles': movie_roles,
                                                    'srednia':srednia,'ocenaR':przekazujeoceny})
        else:
            return render(request, self.template_name, {'movie': Movie.objects.get(id=movie_id),
                                                    'desc': desc, 'roles': Role.objects, 'movie_roles': movie_roles,'srednia':srednia,'ocenaR':przekazujeoceny
            })


def set_rating(request, movie_id=1):
    language = translation.get_language_from_request(request)
    ocena = request.GET['ocena']
    user = request.user.id
    oceny = Rate.objects.filter(movie_id=movie_id, user_id=request.user.id)
    try:
        avg = Avg.objects.get(movie=Movie.objects.get(id=movie_id))
        ilosc = avg.numberOfVotes
        suma = avg.sumVotes
        test = 1
    except Avg.DoesNotExist:
        test = 0
        ilosc = 0
        suma = 0


    if len(oceny) == 0 and test ==0:
        rate = Rate(rate=ocena, user=User.objects.get(id=user), movie=Movie.objects.get(id=movie_id))
        rate.save()
        #ocena2 = rate[0].rate
        ilosc = ilosc + 1
        suma = suma+int(ocena)
        srednia = Avg(movie=Movie.objects.get(id=movie_id), numberOfVotes=ilosc, sumVotes=suma)
        srednia.save()
    elif len(oceny) ==0:
        rate = Rate(rate=ocena, user=User.objects.get(id=user), movie=Movie.objects.get(id=movie_id))
        rate.save()
        ilosc = ilosc + 1
        suma = suma+int(ocena)
        avg.numberOfVotes = ilosc
        avg.sumVotes = suma
        avg.save()
    else:
        ocena2 = oceny[0].rate
        oceny[0].rate = ocena
        suma = suma+int(ocena)-int(ocena2)
        avg.sumVotes = suma
        avg.save()
        oceny[0].save()
    return HttpResponseRedirect(redirect_to='/'+language+'/movies/get/'+movie_id+'/')

def set_role(request):
    language = translation.get_language_from_request(request)
    ocenaR = request.GET['ocenaR']
    role_id = request.GET['role_id']
    movie_id= request.GET['movie_id']
    user = request.user.id
    oceny = RoleRate.objects.filter(role_id=role_id, user_id=request.user.id)


    if len(oceny) == 0:
        rate = RoleRate(rate=ocenaR, user=User.objects.get(id=user), role=MovieRole.objects.get(id=role_id))
        rate.save()


    else:
        oceny[0].rate = ocenaR
        oceny[0].save()


    return HttpResponseRedirect(redirect_to='/'+language+'/movies/get/'+movie_id+'/')