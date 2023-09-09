from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=1000, default="", unique=True, primary_key=True)
    address = models.CharField(max_length=1000, null=True)
    external_auditor = models.CharField(max_length=1000, null=True)
    fiscal_year_length = models.IntegerField(null=False, default=1)
    creation_date = models.DateField(null=True, default=None)
    ipo_date = models.DateField(null=True, default=None)
    social_object = models.CharField(max_length=10000, )
    publications_page = models.CharField(max_length=1000, default="")
    instrument_link = models.CharField(max_length=1000, default="")

class Management(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    name = models.CharField(max_length=1000, default="", unique=False)
    post = models.CharField(max_length=1000, default="", unique=False)

class Shareholder(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    holder = models.CharField(max_length=100, default="", unique=False)
    percentage = models.CharField(max_length=100, default="", unique=False)

class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    name = models.CharField(max_length=1000, default="", unique=False)
    mail = models.CharField(max_length=1000, default="", unique=False)
    phone = models.CharField(max_length=1000, default="", unique=False)
    fax = models.CharField(max_length=1000, default="", unique=False)
    website = models.CharField(max_length=1000, default="", unique=False)

class KeyFigures(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    year = models.CharField(max_length=30, default="", unique=True)
    consolidated_accounts = models.CharField(max_length=30, default="", unique=True)
    share_capital = models.DecimalField(max_digits=10, decimal_places=2)
    equity = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_titles = models.PositiveIntegerField(default=0)
    sales_figures = models.DecimalField(max_digits=10, decimal_places=2)
    operating_result = models.DecimalField(max_digits=10, decimal_places=2)
    net_income = models.DecimalField(max_digits=10, decimal_places=2)

class Ratios(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    year = models.CharField(max_length=30, default="", unique=True)
    bpa = models.DecimalField(max_digits=5, decimal_places=2)
    roe = models.DecimalField(max_digits=5, decimal_places=2)
    payout = models.DecimalField(max_digits=5, decimal_places=2)
    dividend_yield = models.DecimalField(max_digits=5, decimal_places=2)
    per = models.DecimalField(max_digits=5, decimal_places=2)
    pbr = models.DecimalField(max_digits=5, decimal_places=2)

class Dividend(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    year = models.CharField(max_length=30, default="", unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    dividend_type = models.CharField(max_length=30, default="", unique=True)
    ex_date = models.DateField(null=True, default=None)
    payment_date = models.DateField(null=True, default=None)
