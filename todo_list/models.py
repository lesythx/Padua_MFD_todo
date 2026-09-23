from django.db import models

class List(models.Model): 
    item = models.CharField(max_length=200)             #varchar
    completed = models.BooleanField(default=False)      #just a check card

    def __str__(self): #returns the string value
        return self.item


# Create your models here.
