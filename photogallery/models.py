# -*- coding: utf-8 -*-
from django.db import models
from movies.models import Movie
from people.models import Person
from string import join
import os
from PIL import Image as PImage
from Filmland.settings import MEDIA_ROOT


class MovieAlbum(models.Model):
    movie = models.OneToOneField(Movie, verbose_name="Film")

    def __unicode__(self):
        return "%s" % self.movie

    def images(self):
        lst = [x.image.name for x in self.image_set.all()]
        lst = ["<a href='/media/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
        return join(lst, ', ')
    images.allow_tags = True

    class Meta:
        ordering = ['movie']
        verbose_name = 'Album Filmu'
        verbose_name_plural = u'Albumy Filmów'


class PersonAlbum(models.Model):
    person = models.OneToOneField(Person, verbose_name="Osoba")

    def __unicode__(self):
        return "%s" % self.person

    def images(self):
        lst = [x.image.name for x in self.image_set.all()]
        lst = ["<a href='/media/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
        return join(lst, ', ')
    images.allow_tags = True

    class Meta:
        ordering = ['person']
        verbose_name = 'Album Osoby'
        verbose_name_plural = u'Albumy Osób'


class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True, verbose_name="Tytył")
    image = models.FileField(upload_to="images/", verbose_name="Zdjęcia")
    people = models.ManyToManyField(PersonAlbum, blank=True, verbose_name="Osoby")
    movies = models.ManyToManyField(MovieAlbum, blank=True, verbose_name="Filmy")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Data")
    width = models.IntegerField(blank=True, null=True, verbose_name="Wysokość")
    height = models.IntegerField(blank=True, null=True, verbose_name="Szerokość")

    def __unicode__(self):
        return self.image.name

    def save(self, *args, **kwargs):
        """Save image dimensions."""
        super(Image, self).save(*args, **kwargs)
        im = PImage.open(os.path.join(MEDIA_ROOT, self.image.name))
        self.width, self.height = im.size
        super(Image, self).save(*args, ** kwargs)

    def size(self):
        """Image size."""
        return "%s x %s" % (self.width, self.height)

    def people_(self):
        lst = [Person.objects.get(id=x[1]).last_name + " " +
               Person.objects.get(id=x[1]).first_name for x in self.people.values_list()]
        return str(join(lst, ', '))

    def movies_(self):
        lst = [Movie.objects.get(id=x[1]).title for x in self.movies.values_list()]
        return str(join(lst, ', '))

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % \
               (self.image.name, self.image.name)
    thumbnail.allow_tags = True

    class Meta:
        ordering = ['title']
        verbose_name = 'Zdjecie'
        verbose_name_plural = u'Zdjęcia'