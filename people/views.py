from django.shortcuts import render
from people.models import Person, Biography
from movies.models import MovieRole, Role
from django.views.generic import View


class PeopleView(View):
    template_name = 'people.html'

    def get(self, request):
        people_all = Person.objects.order_by('last_name')
        return render(request, self.template_name, {'people': people_all})


class PersonView(View):
    template_name = 'person.html'

    def get(self, request, person_id=1):
        bio = Biography.objects.filter(person_id=person_id)
        movie_roles = MovieRole.objects.filter(people__id=person_id)
        return render(request, self.template_name, {'person': Person.objects.get(id=person_id), 'bio': bio,
                                                    'movie_roles': movie_roles, 'roles': Role.objects})