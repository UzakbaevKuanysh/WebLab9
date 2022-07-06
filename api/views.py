
# Create your views here.
from django import views
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets,generics
from api.models import  Company, Vacancy
from api.serializers import CompanySerializer,  VacancySerializer

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyViewSet_detail(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyViewSet_detail(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacanciesByCompany(generics.ListAPIView):
    serializer_class = VacancySerializer
    def get_queryset(self):
       """
       This view should return a list of all the purchases for
       the user as determined by the username portion of the URL.
       """
       company_id = self.kwargs['id']
       return Vacancy.objects.filter(company=company_id)

class VacanciesSorted(generics.ListAPIView):
    serializer_class = VacancySerializer
    
    def get_queryset(self):
       """
       This view should return a list of all the purchases for
       the user as determined by the username portion of the URL.
       """
       
       return Vacancy.objects.order_by('-salary')[:10]