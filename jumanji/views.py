from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.template import RequestContext

from jumanji.models import Vacancy, Specialty, Company


class MainPageView(View):

    def get(self, request):
        return render(request, 'jumanji/index.html')


class AllVacanciesPageView(ListView):

    model = Vacancy

    def get_template_names(self):
        template_name = 'jumanji/vacancies.html'
        return template_name


class VacancyDetailView(DetailView):

    model = Vacancy

    def get_template_names(self):
        template_name = 'jumanji/vacancy-detail.html'
        return template_name


class SpecialtyVacanciesView(ListView):

    model = Vacancy

    def get_queryset(self):
        specialty = self.kwargs['slug']
        queryset = Vacancy.objects.filter(specialty__code=specialty)
        return queryset

    def get_template_names(self):
        template_name = 'jumanji/specialty.html'
        return template_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        specialty = Specialty.objects.filter(code=self.kwargs['slug'])
        context['title'] = specialty.first().title
        context['vacancies_count'] = self.get_queryset().count()
        return context


class CompanyView(ListView):

    model = Vacancy

    def get_queryset(self):
        company = self.kwargs['id']
        queryset = Vacancy.objects.filter(company__id=company)
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = self.get_queryset().first().company
        context['company'] = company
        return context
 
    def get_template_names(self):
        template_name = 'jumanji/company.html'
        return template_name


def handler404(request, exception, template_name="404.html"):
    response = render(template_name)
    response.status_code = 404
    return response


def handler500(request, exception, template_name="500.html"):
    response = render(template_name)
    response.status_code = 500
    return response