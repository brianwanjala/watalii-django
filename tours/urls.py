from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name= 'list'),
    path('<int:pk>/', views.details, name= 'details'),
    path('<int:pk>/book/', views.book_tour, name= 'book_tour'),
    path('contact/', views.contact, name= "contact")
]