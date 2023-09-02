from django.shortcuts import render
from rest_framework import generics
from .serializers import CompanySerializer
from .models import Company
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home Page")
class DashboardView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
def actionnaire(request):
    return HttpResponse("actionnaire")
def companies(request):
    return HttpResponse("companies")
def chiffres(request):
    return HttpResponse("chiffres")
def ratios(request):
    return HttpResponse("ratios")
def retourner(request):
    return HttpResponse("retourner")
def publications(request):
    return HttpResponse("publications")
def dividende(request):
    return HttpResponse("dividende")
def emissions(request):
    return HttpResponse("emissions")