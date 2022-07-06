from rest_framework import serializers

from api.models import Company, Vacancy


class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ['name', 'description','city','address']
class VacancySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vacancy
        fields = ['name', 'description', 'salary','company']