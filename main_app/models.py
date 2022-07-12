from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    food_category = models.CharField(max_length=100)
    personal_rating = models.IntegerField()

    def __str__(self):
        return self.name