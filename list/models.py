# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class MovieList(models.Model):
    user = models.ForeignKey(User, unique=True, null=True, verbose_name='Użytkownik')

    def __unicode__(self):
        return u"%s" % self.user

    class Meta:
        verbose_name = 'Lista użytkownika'
        verbose_name_plural = 'Listy użytkownika'


class MovieListItem(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nazwa')
    movies = models.ManyToManyField(Movie, blank=True, null=True, verbose_name='Filmy')
    movielist = models.ForeignKey(MovieList, verbose_name='Użytkownik')

    def __unicode__(self):
        return u"%s %s" % (self.name, self.movielist.user)

    class Meta:
        verbose_name = 'Lista'
        verbose_name_plural = 'Listy'