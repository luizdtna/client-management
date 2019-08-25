from django.db import models

# Create your models here.

class Document(models.Model):
    num_doc = models.CharField(max_length=50)

    def __str__(self):
        return self.num_doc

class Pessoa(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    bio = models.TextField(max_length=2000)
    photo = models.ImageField(upload_to ='clients_photos',null = True , blank=True)
    doc = models.OneToOneField(Document, null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name +" "+ self.last_name

class Product(models.Model):
    description = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.description

class Sale(models.Model):
    number = models.CharField(max_length=10)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    taxes = models.DecimalField(max_digits=10, decimal_places=2)
    person = models.ForeignKey(Pessoa, null=True,blank=True,on_delete=models.PROTECT)#se Pessoa ja tiver venda, não permite deletar
    products = models.ManyToManyField(Product,blank=True)
    def __str__(self):
        return self.number