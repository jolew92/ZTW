# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class MovieItem(models.Model):
    user = models.ForeignKey(User, null=True)
    movieitem = models.ForeignKey(Movie, null=True)

    def __unicode__(self):
        return u"%s %s" % (self.user.username, self.movieitem)

    class Meta:
        verbose_name = 'Ulubiony'
        verbose_name_plural = 'Ulubione'


class MovieList(models.Model):
    user = models.ForeignKey(User, unique=True, null=True)
    movielist = models.ManyToManyField(MovieItem, null=True)

    def __unicode__(self):
        return u"%s" % self.user.username

    class Meta:
        verbose_name = 'Lista ulubionych'
        verbose_name_plural = 'Listy ulubionych'