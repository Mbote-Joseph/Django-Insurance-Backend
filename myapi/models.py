
from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    custID = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


    def __str__(self):
        return self.custID