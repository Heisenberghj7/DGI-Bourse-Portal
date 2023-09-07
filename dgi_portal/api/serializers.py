from rest_framework import serializers
from .models import Company, Management, Shareholder, Contact, KeyFigures, Ratios, Dividend

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = '__all__'

class ShareholderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shareholder
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class KeyFiguresSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyFigures
        fields = '__all__'

class RatiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratios
        fields = '__all__'

class DividendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dividend
        fields = '__all__'
