from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from movies.models import Movie
from photogallery.models import Image
from people.models import Person


class MovieGalleryView(View):
    template_name = 'galleryMovie.html'

    def get(self, request, movie_id=1, image_id=1):
        if request.method == 'GET':
            movie = Movie.objects.get(id=movie_id)
            image = Image.objects.get(id=image_id)
            images = Image.objects.filter(movies__movie_id=movie_id).order_by('id')
            im_next = images.filter(id__gt=image_id).order_by('id')[:1]
            im_previous = images.filter(id__lt=image_id).order_by('-id')[:1]
            if not im_next.exists():
                im_next = images.order_by('id')[:1]
            if not im_previous.exists():
                im_previous = images.order_by('-id')[:1]

            return render(request, self.template_name, {'image': image, 'next': im_next, 'previous': im_previous, 'images': images,
                                                        'movie': movie})
        else:
            return HttpResponseRedirect('/')


class PersonGalleryView(View):
    template_name = 'galleryPerson.html'

    def get(self, request, person_id=1, image_id=1):
        if request.method == 'GET':
            person = Person.objects.get(id=person_id)
            image = Image.objects.get(id=image_id)
            images = Image.objects.filter(people__person_id=person_id).order_by('id')
            im_next = images.filter(id__gt=image_id).order_by('id')[:1]
            im_previous = images.filter(id__lt=image_id).order_by('-id')[:1]
            if not im_next.exists():
                im_next = images.order_by('id')[:1]
            if not im_previous.exists():
                im_previous = images.order_by('-id')[:1]

            return render(request, self.template_name, {'image': image, 'next': im_next, 'previous': im_previous, 'images': images,
                                                        'person': person})
        else:
            return HttpResponseRedirect('/')