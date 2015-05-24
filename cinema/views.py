from django.views.generic import View
from django.shortcuts import render
from cinema.models import Cinema,Town,Timetable,Brand


class CinemasView(View):
    template_name = 'cinemas.html'


    def get(self, request):
        if 'brand' in request.GET:
            brand_form = request.GET['brand']
            brands_dict = Brand.objects.values('id').get(name=brand_form)
        else:
            brand_form=""

        if 'town' in request.GET:
            town_form = request.GET['town']
            towns_dict = Town.objects.values('id').get(name=town_form)
        else:
            town_form=""

        if town_form!="" and brand_form!="":
            cinemas=Cinema.objects.filter(town=towns_dict['id'],brand=brands_dict['id'])
        elif town_form!="" and brand_form=="":
            cinemas=Cinema.objects.filter(town=towns_dict['id'])
        elif town_form=="" and brand_form!="":
            cinemas=Cinema.objects.filter(brand=brands_dict['id'])
        else:
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