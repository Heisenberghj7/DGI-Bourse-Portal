from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20, default="", unique=True)
    adress = models.CharField(max_length=100)
    externalAuditor = models.CharField(max_length=50)
    fiscalYearLength = models.IntegerField(null=False, default=1)
    Creation_date = models.DateTimeField()
    Ipo_date = models.DateTimeField()
    Social_object= models.CharField(max_length=1000, unique=True)
