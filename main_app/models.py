from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    food_category = models.CharField(max_length=100)
    yelp_url = models.CharField(max_length=100)
    personal_rating = models.IntegerField(
        validators = [MaxValueValidator(5), MinValueValidator(1)]
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'restaurant_id': self.id})