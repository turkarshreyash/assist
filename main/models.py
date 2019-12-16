from django.db import models

# Create your models here.
class Query(models.Model):
    ip_location = models.CharField(max_length=50)
    text_searched = models.CharField(primary_key=True,max_length=100)
    time = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(primary_key=True,max_length=15)

class Languages(models.Model):
    name = models.CharField(primary_key=True,max_length=75)
    code = models.CharField(max_length=5)

class Countries(models.Model):
    name = models.CharField(primary_key=True,max_length=50)
    code = models.CharField(max_length=5)

class PropertiesOfSearch(models.Model):
    q = models.CharField(max_length=50,null=True)
    query = models.ForeignKey(Query,on_delete=models.CASCADE)
    country = models.ForeignKey(Countries,null = True,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,null = True,on_delete=models.CASCADE)
    language = models.ForeignKey(Languages,null = True,on_delete=models.CASCADE)
    published_from = models.DateTimeField(null=True)
    published_to = models.DateTimeField(null=True)


class LanguagesCountry(models.Model):
    languages = models.ForeignKey(Languages,on_delete=models.CASCADE)
    country = models.ForeignKey(Countries,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('languages', 'country',)

    def __str__(self):
        return (str(self.country)+str(self.languages))