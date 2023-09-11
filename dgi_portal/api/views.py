from rest_framework import generics
from .models import Company, Management, Shareholder, Contact, KeyFigures, Ratios, Dividend, Publications
from .serializers import CompanySerializer, ManagementSerializer, ShareholderSerializer, ContactSerializer, KeyFiguresSerializer, RatiosSerializer, DividendSerializer,PublicationsSerializer

class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class CompanyDetailView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ManagementListView(generics.ListAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer
class ManagementDetailView(generics.RetrieveAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer


class ShareholderListView(generics.ListAPIView):
    queryset = Shareholder.objects.all()
    serializer_class = ShareholderSerializer
class ShareholderDetailView(generics.RetrieveAPIView):
    queryset = Shareholder.objects.all()
    serializer_class = ShareholderSerializer


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
class ContactDetailView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class KeyFiguresListView(generics.ListAPIView):
    queryset = KeyFigures.objects.all()
    serializer_class = KeyFiguresSerializer
class KeyFigureslView(generics.RetrieveAPIView):
    queryset = KeyFigures.objects.all()
    serializer_class = KeyFiguresSerializer



class RatiosListView(generics.ListAPIView):
    queryset = Ratios.objects.all()
    serializer_class = RatiosSerializer
class RatioslView(generics.RetrieveAPIView):
    queryset = Ratios.objects.all()
    serializer_class = RatiosSerializer


class DividendListView(generics.ListAPIView):
    queryset = Dividend.objects.all()
    serializer_class = DividendSerializer
class DividendlView(generics.RetrieveAPIView):
    queryset = Dividend.objects.all()
    serializer_class = DividendSerializer

class PublicationsListView(generics.ListAPIView):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer
class PublicationslView(generics.RetrieveAPIView):
    queryset = Publications.objects.all()
    serializer_class = PublicationsSerializer