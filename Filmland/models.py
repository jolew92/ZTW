from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Filmy"

    def __unicode__(self):
        return self.name

class Genere(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Gatunek"
        verbose_name_plural = "Gatunki"

    def __unicode__(self):
        return self.name

class MovieGenere(models.Model):
    movie = models.ForeignKey(Movies)
    genere = models.ForeignKey(Genere)


OCENA_CHOICE = (
    (1,'Omijac'),
    (2,'Bardzo zly'),
    (3,'Marny'),
    (4,'Slaby'),
    (5,'Moze'),
    (6,'Sredni'),
    (7,'Dobry'),
    (8,'Bardzo dobry'),
    (9,'Wysmienity'),
    (10,'Arcydzielo'),
)

class Vote(models.Model):
    vote = models.IntegerField(choices=OCENA_CHOICE)

class Rating(models.Model):
    movie = models.ForeignKey(Movies)
    rate = models.ForeignKey(Vote)

class Year(models.Model):
    year = models.IntegerField();

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()

class MovieRole(models.Model):
    movie = models.ForeignKey(Movies)
    person = models.ForeignKey(Person)
    role = models.CharField(max_length=50)

class Biography(models.Model):
    bio= models.CharField(max_length=9000)

LANGUAGE_CHOICE = (
    (1,'PL'),
    (2,'ENG'),
)

class Language(models.Model):
    language = models.IntegerField(choices=LANGUAGE_CHOICE)

class Decription(models.Model):
    movie = models.ForeignKey(Movies)
    desc = models.CharField(max_length=9000)

class MovieListItem(models.Model):
    def something(self):
        pass

class User(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

class MovieList(models.Model):
    userList = models.ForeignKey(User)
    movieList = models.ForeignKey(Movies)

USERROLE_CHOICE = (
    (1,'User'),
    (2,'Mod'),
)

class UserRole(models.Model):
    def something(self):
        pass

COUNTRY_CHOICE = (
    (1,'PL'),
    (2,'ENG'),
    (3,'ITA'),
)

class Country(models.Model):
    country = models.IntegerField(choices=COUNTRY_CHOICE)

class MovieCountry(models.Model):
    movie = models.ForeignKey(Movies)
    country = models.ForeignKey(Country)

