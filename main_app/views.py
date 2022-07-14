from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Restaurant

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def restaurants_index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index.html', {
        'restaurants': restaurants
    })

def restaurants_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant
    })

class RestaurantCreate(CreateView):
    model = Restaurant
    fields = '__all__'

class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = '/restaurants/'

class RestaurantUpdate(UpdateView):
    model = Restaurant
    fields = '__all__'