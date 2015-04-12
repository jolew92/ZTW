from django.shortcuts import render_to_response
from people.models import Person, Biography
from movies.models import MovieRole, Role


def people(request):
    people_all = Person.objects.order_by('last_name')
    return render_to_response('people.html', {'people': people_all})


def person(request, person_id=1):
    bio = Biography.objects.filter(person_id=person_id)
    movie_roles = MovieRole.objects.filter(people__id=person_id)
    return render_to_response('person.html', {'person': Person.objects.get(id=person_id), 'bio': bio,
                                              'movie_roles': movie_roles, 'roles': Role.objects})