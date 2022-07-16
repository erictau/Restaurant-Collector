from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Restaurant
from .forms import FoodForm

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
    food_form = FoodForm()
    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant,
        'food_form': food_form
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

def add_food(request, restaurant_id):
    form = FoodForm(request.POST)
    if form.is_valid():
        new_food = form.save(commit=False)
        new_food.restaurant_id = restaurant_id
        new_food.save()
    return redirect('detail', restaurant_id=restaurant_id)