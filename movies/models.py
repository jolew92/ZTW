# -*- coding: utf-8 -*-
from django.db import models
from people.models import Person
from django.core import urlresolvers
from django.contrib.auth.models import User
#from djangoratings.fields import RatingField


class Language(models.Model):
    name = models.CharField(max_length=30, verbose_name='Język')
    name_en = models.CharField(max_length=30, verbose_name='Language')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = u'Język'
        verbose_name_plural = u'Języki'


class Genre(models.Model):
    genre = models.CharField(max_length=30, verbose_name='Gatunek')
    genre_en = models.CharField(max_length=30, verbose_name='Genre')

    def __unicode__(self):
        return unicode(self.genre)

    class Meta:
        ordering = ['genre']
        verbose_name = 'Gatunek'
        verbose_name_plural = 'Gatunki'


VOTE_GRADES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
)


LANGUAGE = (
    ('PL', 'Polski'),
    ('EN', 'English'),
)


class Country(models.Model):
    name = models.CharField(max_length=30, verbose_name='Kraj')
    name_en = models.CharField(max_length=30, verbose_name='Country')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Kraj'
        verbose_name_plural = 'Kraje'


class Movie(models.Model):
    title = models.CharField(max_length=30, verbose_name='Tytuł')
    title_en = models.CharField(max_length=30, verbose_name='Title')
    year = models.IntegerField(max_length=4, blank=False, null=False, verbose_name='Rok')
    language = models.ForeignKey(Language, blank=True, null=True, verbose_name='Język')
    genre = models.ManyToManyField(Genre, blank=True, null=True, verbose_name='Gatunek')
    country = models.ManyToManyField(Country, blank=True, null=True, verbose_name='Kraj')
    #rating = RatingField(range=5)

    def __unicode__(self):
        return unicode(self.title)

    @property
    def get_admin_url(self):
        return urlresolvers.reverse("admin:%s_%s_change" %
        (self._meta.app_label, self._meta.module_name), args=(self.pk,))

    def get_url(self):
        return u"/%s/%s/%s" % (self._meta.app_label, self._meta.module_name, self.pk)

    class Meta:
        ordering = ['title']
        verbose_name = 'Film'
        verbose_name_plural = 'Filmy'


class Role(models.Model):
    role = models.CharField(max_length=30, verbose_name='Rola')
    role_en = models.CharField(max_length=30, verbose_name='Role')

    def __unicode__(self):
        return unicode(self.role)

    class Meta:
        ordering = ['role']
        verbose_name = 'Rola'
        verbose_name_plural = 'Role'


class MovieRole(models.Model):
    role = models.ForeignKey(Role)
    people = models.ManyToManyField(Person, blank=True, null=True, verbose_name='Osoba')
    movie = models.ForeignKey(Movie, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.role)

    class Meta:
        ordering = ['role']
        verbose_name = 'Rola'
        verbose_name_plural = 'Role'


class Description(models.Model):
    movie = models.ForeignKey(Movie)
    description = models.TextField(verbose_name='Opis filmu')
    language = models.CharField(max_length=2, choices=LANGUAGE, default='PL', verbose_name='Język')

    def __unicode__(self):
        return u"%s %s %s" % (self.movie.title, self.movie.year, self.language)

    class Meta:
        verbose_name = 'Opis filmu'
        verbose_name_plural = 'Opisy filmów'


class Rate(models.Model):
    rate = models.CharField(max_length=2, choices=VOTE_GRADES, verbose_name='Oceny')
    user = models.ForeignKey(User, null=True)
    movie = models.ForeignKey(Movie)

    def __unicode__(self):
        return u"%s %s %s" % (self.movie.title, self.user, self.rate)

    class Meta:
        verbose_name = 'Ocena filmu'
        verbose_name_plural = 'Oceny filmów'