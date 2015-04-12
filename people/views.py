from django.shortcuts import render_to_response
from people.models import Person


def people(request):
    people_all = Person.objects.order_by('last_name')
    return render_to_response('people.html', {'people': people_all})


def person(request, person_id=1):
    return render_to_response('person.html', {'person': Person.objects.get(id=person_id)})