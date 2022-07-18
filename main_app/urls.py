from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/<int:restaurant_id>/', views.restaurants_detail, name='detail'),
    path('restaurants/create/', views.RestaurantCreate.as_view(), name='restaurants_create'),
    path('restaurants/<int:pk>/delete/', views.RestaurantDelete.as_view(), name='restaurants_delete'),
    path('restaurants/<int:pk>/update/', views.RestaurantUpdate.as_view(), name='restaurants_update'),
    path('restaurants/<int:restaurant_id>/add_food/', views.add_food, name='add_food'),
    path('certifications/', views.CertificationList.as_view(), name='certification_index'),
    path('certifications/create/', views.CertificationCreate.as_view(), name='certification_create'),
    path('certifications/<int:pk>/', views.CertificationDetail.as_view(), name='certification_detail'),
    path('certifications/<int:pk>/delete', views.CertificationDelete.as_view(), name='certification_delete'),
    path('restaurants/<int:restaurant_id>/certifications/<int:certification_id>', views.assoc_certification, name='assoc_certification')
]