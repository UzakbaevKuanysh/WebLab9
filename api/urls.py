from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import VacanciesByCompany, VacanciesSorted, VacancyViewSet, VacancyViewSet_detail, CompanyViewSet, CompanyViewSet_detail
vacancies = VacancyViewSet.as_view({
  'get': 'list',
  'post': 'create'
})
vacancy_detail = VacancyViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    
})

companies = CompanyViewSet.as_view({
  'get': 'list',
  'post': 'create'
})
company_detail = CompanyViewSet_detail.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
    
})

urlpatterns = [
    path('companies/', companies, name = 'companies'),
    path('companies/<int:pk>', company_detail, name = "company_detail"),
    path('vacancies/', vacancies, name = 'vacancies'),
    path('vacancies/<int:pk>', vacancy_detail, name = "vacancy_detail"),
    path('companies/<int:id>/vacancies', VacanciesByCompany.as_view(), name = "vacancy_companies"),
    path('vacancies/top_ten', VacanciesSorted.as_view(), name = "vacancy_top_ten")
]
urlpatterns = format_suffix_patterns(urlpatterns)
