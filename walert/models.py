from django.db import models

# Create your models here.
class CityData(models.Model):
    name=models.CharField(max_length=200)
    mintemp=models.DecimalField(max_digits=5, decimal_places=2)
    maxtemp=models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "%s %s %s" %(self.name,self.mintemp,self.maxtemp)
    

class AlertData(models.Model):
    alertmsg=models.CharField(max_length=100)

    def __str__(self):
        return "%s" %(self.alertmsg)