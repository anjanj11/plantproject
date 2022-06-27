from django.db import models

# Create your models here.
class Plant:
    planttype=models.CharField(max_length=200)
    plantprice=models.IntegerField()
    quantity=models.IntegerField


    def __str__(self):
        return self.planttype

