from django.db import models

# Create your models here.
class Search(models.Model):
    pk = models.AutoField(primary_key=True)
    ip_location = models.CharField(max_length=50)
    text_searched = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=15)

class Languages(models.Model):
    name = models.CharField(max_length=75)


class Countries(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    capital_city = models.CharField(max_length=50)
    language = models.ForeignKey(Languages,on_delete=models.CASCADE)

class PropertiesOfSearch(models.Model):
    q = models.CharField(max_length=50)
    country = models.ForeignKey(Languages,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    language = models.ForeignKey(Languages,on_delete=models.CASCADE)

