from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_meal/", views.add_meal, name="add-meal"),
    path("update_meal/<int:pk>/", views.update_meal, name="update-meal"),
    path("delete_meal/<int:pk>/", views.delete_meal, name="delete-meal"),
    path("data_meal/<int:pk>/", views.data_meal, name="data-meal"),
    path("add_food/", views.add_food, name="add-food"),
    path("food_list/", views.food_list, name="food-list"),
]
