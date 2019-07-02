from django.db import models

class moviedata(models.Model):
    movie_id = models.IntegerField()
    movie_name = models.CharField(max_length=50)
    movie_cast = models.CharField(max_length=100)
    movie_rating = models.IntegerField()
    movie_feedback = models.CharField(max_length=500)