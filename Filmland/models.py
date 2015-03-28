from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=30)

class Genere(models.Model):
    name = models.CharField(max_length=30)

class MovieGenere(models.Model):
    movie = models.ForeignKey(Movies)
    genere = models.ForeignKey(Genere)



class Rating(models.Model):
    movie = models.ForeignKey(Movies)
    rate = models.ForgeinKey(Vote)

ocena_choices = (
    ('1','Omijać'),
    ('2','Bardzo zły'),
    ('3','Marny'),
    ('4','Słaby'),
    ('5','Może'),
    ('6','Średni'),
    ('7','Dobry'),
    ('8','Bardzo dobry'),
    ('9','Wyśmienity'),
    ('10','Arcydzieło'),
)

class Vote(models.Model):
    COS Z CZOISAMI ALE JESZCZE NIE WIEM

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
    NIE WIEM

class Language(models.Model):
    TU TEZ COS Z CHOISAMI?

class Decription(models.Model):
    movie = models.ForeignKey(Movies)
    desc = models.CharField(max_length=255) //tymczasowo

class MovieListItem(models.Model):

class MovieList(models.Model):

class User(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

class UserRole(models.Model):
    TU TEZ COS Z CHOISAMI?

class Country(models.Model):
    TU TEZ COS Z CHOISAMI?

class MovieCountry(models.Model):
    movie = models.ForeignKey(Movies)
    country = models.ForeignKey(Country)

