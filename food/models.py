from django.db import models


class Food(models.Model):
    name = models.CharField(verbose_name="Name", max_length=128)
    calories = models.FloatField(verbose_name="Calories (kcal)")
    total_fat = models.FloatField(verbose_name="Total Fat (g)")
    saturated_fat = models.FloatField(verbose_name="Saturated Fat (g)", default=0)
    cholesterol = models.FloatField(verbose_name="Cholesterol (mg)", default=0)
    sodium = models.FloatField(verbose_name="Sodium (mg)", default=0)
    total_carbohydrate = models.FloatField(
        verbose_name="Total Carbohydrate (g)", default=0
    )
    dietary_fibre = models.FloatField(verbose_name="Dietary Fibre (g)", default=0)
    sugar = models.FloatField(verbose_name="Sugar (g)", default=0)
    protein = models.FloatField(verbose_name="Protein (g)", default=0)

    def __str__(self):
        return "%s" % self.name


class Meal(models.Model):
    BREAKFAST = 1
    MORNING_SNACK = 2
    LUNCH = 3
    AFTERNOON_SNACK = 4
    DINNER = 5
    EVENING_SNACK = 6
    MEAL_TIME_TYPES = (
        (BREAKFAST, "Breakfast"),
        (MORNING_SNACK, "Morning Snack"),
        (LUNCH, "Lunch"),
        (AFTERNOON_SNACK, "Afternoon Snack"),
        (DINNER, "Dinner"),
        (EVENING_SNACK, "Evening Snack"),
    )
    food = models.ForeignKey(Food, verbose_name="Food", on_delete=models.CASCADE)
    serving_size = models.IntegerField(verbose_name="Serving Size")
    meal_time = models.IntegerField(verbose_name="Meal Time", choices=MEAL_TIME_TYPES)

    def __str__(self):
        return "%s" % self.food
