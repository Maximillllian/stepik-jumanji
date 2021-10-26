from django.urls import path

from .views import MainPageView, AllVacanciesPageView, VacancyDetailView, SpecialtyVacanciesView, CompanyView, VacancyDetailView

urlpatterns = [
    path('', MainPageView.as_view(), name="main"),
    path('vacancies/', AllVacanciesPageView.as_view(), name="all_vacancies"),
    path('vacancies/<int:pk>', VacancyDetailView.as_view(), name="vacancy_detail"),
    path('vacancies/cat/<slug:slug>', SpecialtyVacanciesView.as_view(), name="specialization_vacancies"),
    path('company/<int:id>', CompanyView.as_view(), name="company")
]
