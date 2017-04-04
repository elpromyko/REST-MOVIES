from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    directors = models.ForeignKey(Person, related_name='director')
    actors = models.ManyToManyField(Person, through='Role')
    year = models.IntegerField()

    def __str__(self):
        return self.title

class Role(models.Model):
    person = models.ForeignKey(Person, related_name='person')
    movie = models.ForeignKey(Movie)
    role = models.CharField(max_length=64)

    def __str__(self):
        return self.role

