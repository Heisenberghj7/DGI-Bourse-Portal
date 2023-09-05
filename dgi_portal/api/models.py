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
    Publications_page=models.CharField(max_length=150,default="")
    instrument_link=models.CharField(max_length=150,default="")

class Management(models.Model):
    company_name= models.CharField(max_length=20, default="", unique=True) # forign key to Company.name
    name= models.CharField(max_length=20, default="", unique=True)
    post= models.CharField(max_length=20, default="", unique=True)

class shareholders(models.Model):
    name= models.CharField(max_length=20, default="", unique=True) # forign key to Company.name
    holder= models.CharField(max_length=20, default="", unique=True)
    pourcentage= models.FloatField()
    
class Contact(models.Model):
    company_name= models.CharField(max_length=20, default="", unique=True) # forign key to Company.name
    name=models.CharField(max_length=30, default="", unique=True)
    mail=models.CharField(max_length=30, default="", unique=True)
    phone=models.CharField(max_length=20, default="", unique=True)
    fax=models.CharField(max_length=20, default="", unique=True)
    website=models.CharField(max_length=30, default="", unique=True)

class Key_figures(models.Model):
    name= models.CharField(max_length=30, default="", unique=True) # forign key to Company.name
    year= models.CharField(max_length=30, default="", unique=True)
    Consolidated_accounts= models.CharField(max_length=30, default="", unique=True)
    Share_capital= models.CharField(max_length=30, default="", unique=True)
    Equity= models.CharField(max_length=30, default="", unique=True)
    Number_of_titles= models.CharField(max_length=30, default="", unique=True)
    Sales_figures= models.CharField(max_length=30, default="", unique=True)
    Operating_result= models.CharField(max_length=30, default="", unique=True)
    Net_income= models.CharField(max_length=30, default="", unique=True)

class Ratios(models.Model):
    name= models.CharField(max_length=30, default="", unique=True) # forign key to Company.name
    year= models.CharField(max_length=30, default="", unique=True)
    BPA= models.CharField(max_length=30, default="", unique=True)
    ROE= models.CharField(max_length=30, default="", unique=True)
    Payout= models.CharField(max_length=30, default="", unique=True)
    Dividend_yield= models.CharField(max_length=30, default="", unique=True)
    PER= models.CharField(max_length=30, default="", unique=True)
    PBR= models.CharField(max_length=30, default="", unique=True)

class Dividend(models.Model):
    name= models.CharField(max_length=30, default="", unique=True) # forign key to Company.name
    year= models.CharField(max_length=30, default="", unique=True)
    amount= models.CharField(max_length=30, default="", unique=True)
    Dividend_type= models.CharField(max_length=30, default="", unique=True)
    Ex_date= models.CharField(max_length=30, default="", unique=True)
    Payment_date= models.CharField(max_length=30, default="", unique=True)
