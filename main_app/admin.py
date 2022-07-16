from django.contrib import admin
from .models import Food, Restaurant

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Food)