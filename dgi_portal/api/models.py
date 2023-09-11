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
    year = models.CharField(max_length=100, default="", unique=False)
    consolidated_accounts = models.CharField(max_length=100, default="", unique=False)
    share_capital = models.CharField(max_length=100, default="", unique=False)
    equity = models.CharField(max_length=100, default="", unique=False)
    number_of_titles = models.CharField(max_length=100, default="", unique=False)
    sales_figures = models.CharField(max_length=100, default="", unique=False)
    operating_result = models.CharField(max_length=100, default="", unique=False)
    net_income = models.CharField(max_length=100, default="", unique=False)

class Ratios(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    year = models.CharField(max_length=100, default="", unique=False)
    bpa = models.CharField(max_length=100, default="", unique=False)
    roe = models.CharField(max_length=100, default="", unique=False)
    payout = models.CharField(max_length=100, default="", unique=False)
    dividend_yield = models.CharField(max_length=100, default="", unique=False)
    per = models.CharField(max_length=100, default="", unique=False)
    pbr = models.CharField(max_length=100, default="", unique=False)

class Dividend(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    year = models.CharField(max_length=100, default="", unique=False)
    amount = models.CharField(max_length=100, default="", unique=False)
    dividend_type = models.CharField(max_length=100, default="", unique=False)
    ex_date = models.DateField(null=True, default=None)
    payment_date = models.DateField(null=True, default=None)

class Publications(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    date = models.DateField(null=True, default=None)
    title = models.CharField(max_length=100, default="", unique=False)
    link = models.CharField(max_length=1000, default="", unique=False)
    doc_info = models.CharField(max_length=1000, default="", unique=False)
    