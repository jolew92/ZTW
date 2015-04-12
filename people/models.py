# -*- coding: utf-8 -*-
from django.db import models

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


class Biography(models.Model):
    person = models.ForeignKey(Person)
    description = models.TextField(verbose_name='Biografia')
    language = models.CharField(max_length=2, choices=LANGUAGE, default='PL', verbose_name='Język')

    def __unicode__(self):
        return u"%s %s %s" % (self.person.last_name, self.person.first_name, self.language)

    class Meta:
        verbose_name = 'Biografia'
        verbose_name_plural = 'Biografie'

