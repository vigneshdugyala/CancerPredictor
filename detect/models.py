from django.db import models

class Person(models.Model):
    name= models.CharField(max_length=200)
    gender= models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.CharField(max_length=200)
