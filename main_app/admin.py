from django.contrib import admin
from .models import Food, Restaurant, Certification

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Certification)