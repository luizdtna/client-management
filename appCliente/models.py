from django.db import models

# Create your models here.

class Pessoa(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    bio = models.TextField(max_length=2000)
    photo = models.ImageField(upload_to ='clients_photos',null = True , blank=True)
    def __str__(self):
        return self.first_name +" "+ self.last_name