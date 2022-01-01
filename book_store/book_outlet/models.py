from django.db import models
from django.db.models.fields import CharField

class Book(models.Model):
    title = CharField(max_length= 50)
    rating = models.IntegerField()
    
    
    
