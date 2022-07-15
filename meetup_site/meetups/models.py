from configparser import MAX_INTERPOLATION_DEPTH
from enum import unique
from django.db import models
from django.forms import CharField, SlugField

# Create your models here.

class Location(models.Model):
    location=models.CharField(max_length=200)
    address=models.CharField(max_length=300)

    def __str__(self):
        return f'{self.location} ({self.address})'
 
class Participant(models.Model):
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.email
        


class meetup(models.Model):
        title=models.CharField(max_length=200)
        organizerEmail=models.EmailField()
        date=models.DateField()
        slug=models.SlugField(unique=True)
        description=models.TextField()
        image=models.ImageField(upload_to='images')
        location=models.ForeignKey(Location, on_delete=models.CASCADE)
        participant=models.ManyToManyField(Participant, blank=True, null=True)

        def __str__(self):
            return f'{self.title} - {self.slug}'
