from django.shortcuts import render
from people.models import Person


def people_list(request):
    people = Person.objects.order_by('last_name')
    return render(request, 'people_list.html', {'people': people})