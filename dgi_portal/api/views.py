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

""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""