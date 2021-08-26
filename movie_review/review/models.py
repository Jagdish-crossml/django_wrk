from django.db import models
from django.db.models.base import Model
from django.db.models.fields import  DateField, DateTimeField, IntegerField

# Create your models here.
class Award(models.Model):
    awname = models.CharField(max_length=50)
    date = models.DateTimeField()       

    def __str__(self):
        return self.awname

class Artist(models.Model):
    aname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    GENDER=[('male','male'),
    ('female','female')]
    gender = models.CharField(max_length=50,choices=GENDER,default='male')
    awards_receieve = models.ManyToManyField(Award)

    def __str__(self):
        return self.aname

class Movie(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    avg_rating = models.DecimalField(max_digits=4,decimal_places=2)
    language = models.CharField(max_length=50)
    length = models.DecimalField(max_digits=4,decimal_places=2)
    artists = models.ManyToManyField(Artist) 
    awards = models.ManyToManyField(Award)

    def __str__(self):
        return self.name


class Rating(models.Model):
    RATINGS =[('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10')
    ]
    movie_rating = models.CharField(max_length=20,choices=RATINGS,default='0')
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    votes = models.IntegerField(default='0')
    def __str__(self):
        return self.movie_rating 