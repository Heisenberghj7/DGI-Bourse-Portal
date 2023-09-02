from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name','adress', 'externalAuditor', 'fiscalYearLength', 'Creation_date',
                  'Ipo_date', 'Social_object')
        
        