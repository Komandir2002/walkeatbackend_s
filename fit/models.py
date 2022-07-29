from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Menu(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=100)
    calories = models.IntegerField()
    price = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def tag_list(self):
        return [i.name for i in self.tags.all()]

