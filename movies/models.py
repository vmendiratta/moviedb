from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models

from . import choices


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.SmallIntegerField(choices=choices.GENDER)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    genre = models.ManyToManyField(Genre)
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, null=True, blank=True)
    alternate_name = models.CharField(max_length=100, null=True, blank=True)
    release_date = models.DateField()
    plot = models.TextField(max_length=5000)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('movie-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name


class Character(models.Model):
    movie = models.ForeignKey(Movie)
    actor = models.ForeignKey(Actor)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return "%s as %s" % (self.actor, self.name)
