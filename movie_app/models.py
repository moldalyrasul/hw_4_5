from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
from rest_framework.exceptions import ValidationError


class Director(models.Model):
    name = models.CharField(max_length=50)

    @property
    def count_movies(self):
        return self.movie.all().count()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.DurationField(null=True, blank=True, verbose_name='Durations')
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def reviews(self):
        review = Review.objects.filter(movie=self)
        return [{'text'} for i in review]

    @property
    def rating(self):
        return Review.objects.filter(movie=self).aggregate(Avg("stars"))


class Review(models.Model):
    text = models.TextField(null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='reviews')
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)

    def __str__(self):
        return self.text
