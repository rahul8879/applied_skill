

# Create your models here.
from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100,default='Ram')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=50)
    experience = models.IntegerField()
    education = models.CharField(max_length=50)
    comments = models.TextField()

    def __str__(self):
        return self.name

