from django.urls import path, re_path

from .views import CreateVacancyView, MainPageView, AllVacanciesPageView, VacancyDetailView, \
    SpecialtyVacanciesView, CompanyView, VacancyApplicationView, StartCompanyView, \
    MyCompanyView, CreateCompanyView, MyCompanyVacanciesView, UpdateVacancyView, \
    CreateVacancyView, ApplicationSendView, MyResumeView, LetsStartResumeView, CreateResumeView, \
    SearchPageView
    

urlpatterns = [
    path('', MainPageView.as_view(), name="main"),
    path('vacancies/', AllVacanciesPageView.as_view(), name="all_vacancies"),
    path('vacancies/<int:pk>', VacancyApplicationView.as_view(), name="vacancy_detail"),
    path('vacancies/<int:pk>/send', ApplicationSendView.as_view(), name="application_send"),
    path('vacancies/cat/<slug:slug>', SpecialtyVacanciesView.as_view(), name="specialty_vacancies"),
    path('company/<int:id>', CompanyView.as_view(), name="company"),
    path('mycompany/', MyCompanyView.as_view(), name="mycompany"),
    path('mycompany/letsstart/', StartCompanyView.as_view(), name="letsstart_company"),
    path('mycompany/create', CreateCompanyView.as_view(), name="create-company"),
    path('mycompany/vacancies/', MyCompanyVacanciesView.as_view(), name="mycompany-vacancies"),
    path('mycompany/vacancies/<int:pk>', UpdateVacancyView.as_view(), name="update_vacancy"),
    path('mycompany/vacancies/create', CreateVacancyView.as_view(), name="create_vacancy"),
    path('myresume/', MyResumeView.as_view(), name="myresume"),
    path('myresume/letsstart', LetsStartResumeView.as_view(), name="letsstart_resume"),
    path('myresume/create', CreateResumeView.as_view(), name="create-resume"),
    path('search', SearchPageView.as_view(), name="search")
]
