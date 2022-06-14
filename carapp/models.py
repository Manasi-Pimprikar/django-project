from django.db import models
from operator import mod

# Create your models here.
class car(models.Model):
    model_name=models.CharField(max_length=100)
    model_number=models.CharField(max_length=40)
    model_prize=models.PositiveIntegerField()

    def __str__(self):
        return self.model_name

class owner(models.Model):
    owner_name=models.CharField(max_length=100)
    owner_mobile=models.CharField(max_length=15)

    def __str__(self):
        return self.owner_name

class order(models.Model):
    owner = models.ForeignKey(owner,on_delete=models.CASCADE)
    car = models.ForeignKey(car,on_delete=models.CASCADE)
    unit = models.PositiveIntegerField()

    def __str__(self):
        return self.owner.owner_name + ' ' +self.car.model_name
