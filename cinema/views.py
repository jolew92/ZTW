from django.views.generic import View
from django.shortcuts import render
from cinema.models import Cinema,Town,Timetable,Brand

class CinemasView(View):
    template_name = 'cinemas.html'


    def get(self, request):
        cinemas=Cinema.objects.order_by('brand')
        brands=Brand.objects.order_by('name')
        towns=Town.objects.order_by('name')
        return render(request, self.template_name, {'cinemas': cinemas,'brands':brands,'towns':towns})

class CinemaView(View):
    template_name = 'cinema.html'

    def get(self, request,cinema_id=1):

        cinema = Cinema.objects.get(id=cinema_id)

        tt = Timetable.objects.filter(cinema=cinema_id)

        return render(request, self.template_name,{'cinema':cinema,'timetable':tt})