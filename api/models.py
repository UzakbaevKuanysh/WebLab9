from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 100)   
    description = models.TextField(max_length=150)
    city = models.CharField(max_length=50)
    address = models.TextField(max_length=150)
    def __str__(self):
        return self.name
# Create your models here.
class Vacancy(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length=150)
    salary = models.FloatField(max_length=50)
    company = models.ForeignKey(Company, blank = True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name