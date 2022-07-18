from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView

from .models import Certification, Restaurant
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
    cert_id_list = restaurant.certifications.all().values_list('id')
    certs_not_owned = Certification.objects.exclude(id__in=cert_id_list)

    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant,
        'food_form': food_form,
        'certs_not_owned': certs_not_owned
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

class CertificationList(ListView):
    model = Certification

class CertificationCreate(CreateView):
    model = Certification
    fields = '__all__'

class CertificationDetail(DetailView):
    model = Certification

class CertificationDelete(DeleteView):
    models = Certification
    success_url = '/certifications/'

def assoc_certification(request, restaurant_id, certification_id):
    Restaurant.objects.get(id=restaurant_id).certifications.add(certification_id)
    return redirect('detail', restaurant_id=restaurant_id)

