from django.db import models

from walkeat import settings
from phonenumber_field.modelfields import PhoneNumberField


categories_choice = (
    ("sets", "sets"),
    ("lunch", "lunch"),
    ("breakfast", "breakfast"),
    ("dinner", "dinner"),
    ("salad", "salad"),
    ("drink", "drink"),
)

week_choices = (
    ("monday", "monday"),
    ("tuesday", "tuesday"),
    ("wednesday", "wednesday"),
    ("thursday", "thursday"),
    ("friday", "friday"),
    ("saturday", "saturday"),
    ("sunday", "sunday"),
)

class Category(models.Model):
    category = models.CharField(choices=categories_choice, max_length=255, unique=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

class Fit(models.Model):
    photo = models.ImageField(default="media/food.svg", upload_to="uploaded_media")
    title = models.CharField(max_length=35)
    calories = models.FloatField(default=0.0)
    carbohydrates = models.FloatField(default=0.0)
    protein = models.FloatField(default=0.0)
    fats = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    ingredients = models.CharField(max_length=255)
    kcal = models.FloatField(default=0.0)
    category = models.ManyToManyField(Category, related_name="categories")

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    food = models.ManyToManyField(Fit,related_name='foods')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        price = self.food.get().price
        food = self.food.filter(price).all()
        return food

    def get_name_food(self):
        food = self.food.all().values()
        return food

    def __str__(self):
        return f"{self.user} cart"



class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False)
    address = models.CharField(max_length=255)
    note = models.CharField(max_length=255, null=True)


    def __str__(self):
        return self.cart