from django.db import models

# Create your models here.
class Student(models.Model):
    id        = models.IntegerField(primary_key=True )
    firstname = models.TextField()
    lastname  = models.TextField()
    passed    = models.BooleanField()
    