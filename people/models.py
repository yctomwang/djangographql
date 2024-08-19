from django.db import models

# Create your models here.
from django.db import models

class Address(models.Model):
    STATE_CHOICES = [
        ('NY', 'New York'),
        ('CA', 'California'),
        # Add more states as needed
    ]
    number = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)

class Person(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
