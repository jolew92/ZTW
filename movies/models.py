# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    name = models.CharField(max_length=30, verbose_name='Język')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Język'
        verbose_name_plural = 'Języki'


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


class Genre(models.Model):
    genre = models.CharField(max_length=30, verbose_name='Gatunek')

    def __unicode__(self):
        return unicode(self.genre)

    class Meta:
        ordering = ['genre']
        verbose_name = 'Gatunek'
        verbose_name_plural = 'Gatunki'


LANGUAGE = (
    ('PL', 'Polski'),
    ('EN', 'English'),
)


class Person(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Imię')
    last_name = models.CharField(max_length=50, verbose_name='Nazwisko')
    birthday = models.DateField(blank=True, null=True, verbose_name='Data urodzenia')

    def __unicode__(self):
        return u"%s %s" % (self.last_name, self.first_name)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Osoba'
        verbose_name_plural = 'Osoby'


class Country(models.Model):
    name = models.CharField(max_length=30, verbose_name='Kraj')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Kraj'
        verbose_name_plural = 'Kraje'


class Movie(models.Model):
    title = models.CharField(max_length=30, verbose_name='Tytuł')
    year = models.IntegerField(max_length=4, blank=False, null=False, verbose_name='Rok')
    language = models.ForeignKey(Language, blank=True, null=True, verbose_name='Język')
    genre = models.ManyToManyField(Genre, blank=True, null=True, verbose_name='Gatunek')
    country = models.ManyToManyField(Country, blank=True, null=True, verbose_name='Kraj')
 #   roles = models.ManyToManyField(Role, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        ordering = ['title']
        verbose_name = 'Film'
        verbose_name_plural = 'Filmy'


class Role(models.Model):
    role = models.CharField(max_length=30, verbose_name='Rola')

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


class Biography(models.Model):
    person = models.ForeignKey(Person)
    description = models.TextField(verbose_name='Biografia')
    language = models.CharField(max_length=2, choices=LANGUAGE, default='PL', verbose_name='Język')

    def __unicode__(self):
        return u"%s %s %s" % (self.person.last_name, self.person.first_name, self.language)

    class Meta:
        verbose_name = 'Biografia'
        verbose_name_plural = 'Biografie'


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