from django.db import models
from movies.models import Movie


class Town(models.Model):
    name = models.CharField(max_length=30, verbose_name='Miasto')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = u'Miasto'
        verbose_name_plural = u'Miasta'


class Brand(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'Siec')

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = u'Siec'
        verbose_name_plural = u'Sieci'


class Cinema(models.Model):
    brand = models.ForeignKey(Brand, verbose_name=u'Siec')
    additionalName = models.CharField(null=True, blank=True, max_length=30, verbose_name='Dodatkowa nazwa')
    town = models.ForeignKey(Town, verbose_name='Miasto')
    street = models.CharField(max_length=30, verbose_name='Ulica')
    street_number = models.CharField(max_length=30, verbose_name='Nr')

    def __unicode__(self):
        return u"%s %s %s" % (self.brand, self.additionalName, self.town.name)

    class Meta:
        ordering = ['brand']
        verbose_name = u'Kino'
        verbose_name_plural = u'Kina'

SALE_SALE = (
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
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
)


class Timetable(models.Model):
    cinema = models.ForeignKey(Cinema, verbose_name='Kino')
    movie = models.ForeignKey(Movie)
    sala = models.CharField(max_length=2, default=1, choices=SALE_SALE, verbose_name='Sala')

    def __unicode__(self):
        return u"%s %s %s" % (self.cinema, self.movie.title, self.sala)

    class Meta:
        ordering = ['cinema']
        verbose_name = u'Film w kinie'
        verbose_name_plural = u'Filmy w kinach'


class Seans(models.Model):
    movieInCinema = models.ForeignKey(Timetable, verbose_name='Film w kinie')
    seans_time = models.TimeField()

    def __unicode__(self):
        return u"%s %s Sala: %s Czas: %s" % (self.movieInCinema.movie.title, self.movieInCinema.cinema,
                                             self.movieInCinema.sala, self.seans_time)

    class Meta:
        ordering = ['movieInCinema']
        verbose_name = u'Repertuar'
        verbose_name_plural = u'Repertuary'