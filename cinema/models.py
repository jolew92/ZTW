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
    additionalName = models.CharField(null=True,blank=True,max_length=30, verbose_name='Dodatkowa nazwa')
    town = models.ForeignKey(Town, verbose_name='Miasto')
    street = models.CharField(max_length=30, verbose_name='Ulica')
    street_number = models.CharField(max_length=30, verbose_name='Nr')

    def __unicode__(self):
        return u"%s %s %s" % (self.brand,self.additionalName, self.town.name)

    class Meta:
        ordering = ['brand']
        verbose_name = u'Kino'
        verbose_name_plural = u'Kina'

class Timetable(models.Model):
    cinema = models.ForeignKey(Cinema, verbose_name='Kino')
    time = models.TimeField()
    movie = models.ForeignKey(Movie)

    def __unicode__(self):
        return u"%s %s %s" % (self.cinema, self.time, self.movie.title)

    class Meta:
        ordering = ['cinema']
        verbose_name = u'Repertuar'
        verbose_name_plural = u'Repertuary'