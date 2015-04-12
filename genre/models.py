from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=30, verbose_name='Gatunek')

    def __unicode__(self):
        return unicode(self.genre)

    class Meta:
        ordering = ['genre']
        verbose_name = 'Gatunek'
        verbose_name_plural = 'Gatunki'