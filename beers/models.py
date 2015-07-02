from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class BeerType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Brewery(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Beer(models.Model):
    name = models.CharField(max_length=200)
    brewery = models.ForeignKey(Brewery)
    beer_type = models.ForeignKey(BeerType)
    tasting_date = models.DateField(null=True, blank=True)
    score = models.IntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ])
    picture = models.ImageField(upload_to='beers')

    def __unicode__(self):
        return self.name
