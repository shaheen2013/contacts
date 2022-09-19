from django.db import models

class Country(models.Model):
       name = models.CharField(max_length=120)
       
       def __str__(self) -> str:
              return self.name

class Contact(models.Model):
       country = models.ForeignKey(Country, on_delete=models.CASCADE)
       phone = models.CharField(max_length=20)
       
       