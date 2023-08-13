from django.shortcuts import render, redirect
from .models import Meal, Food
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import MealForm, FoodForm

# from django.http import HttpResponse


# Create your views here.
def index(request):
    meals = Meal.objects.all()
    context = {"meals": meals, "page_title": "My Food Tracker"}
    return render(request, "list.html", context)


def add_meal(request):
    template = "add_meal.html"
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy("food:index"))
    else:
        context = {"meal_form": MealForm(), "page_title": "Add New Meal"}
        return render(request, template, context)


def delete_meal(request, pk):
    meal = Meal.objects.get(id=pk)
    meal.delete()
    return redirect("food:index")


def update_meal(request, pk):
    template = "update_meal.html"
    meal = Meal.objects.get(id=pk)
    if request.method == "POST":
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy("food:index"))
    else:
        context = {"meal_form": MealForm(instance=meal), "page_title": "Update Meal"}
        return render(request, template, context)


def data_meal(request, pk):
    template = "data_meal.html"
    meal = Meal.objects.get(id=pk)
    context = {"meal": meal, "page_title": "Meal Information"}
    return render(request, template, context)


def add_food(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy("food:index"))
    else:
        context = {"food_form": FoodForm(), "page_title": "Add New Food"}
        return render(request, "add_food.html", context)


def food_list(request):
    foods = Food.objects.all()
    context = {"foods": foods, "page_title": "Available Foods"}
    return render(request, "food_list.html", context)
