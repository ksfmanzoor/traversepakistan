from django.db import models
from geoposition.fields import GeopositionField
from taggit.managers import TaggableManager


class Region(models.Model):
    name = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Place(models.Model):
    category = models.ForeignKey(Category)
    region = models.ForeignKey(Region)
    name = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    coverImage = models.CharField(max_length=256)
    description = models.TextField()
    gettingThere = models.TextField()
    featured = models.BooleanField()
    location = GeopositionField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.name
