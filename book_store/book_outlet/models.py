from django.db import models
from django.db.models.fields import CharField
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    title = CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null = True, max_length=100)
    is_bestselling = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.title} (self.rating) "