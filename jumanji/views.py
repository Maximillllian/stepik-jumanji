from django import template
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.template import RequestContext
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.db.models import Q

from jumanji.models import Application, Vacancy, Specialty, Company, Resume
from .forms import CompanyForm, VacancyForm, ContactUsForm, ResumeForm


class MainPageView(ListView):
    model = Specialty
    template_name = 'jumanji/index.html'


class AllVacanciesPageView(ListView):
    model = Vacancy
    template_name = 'jumanji/vacancies.html'


class CreateAapplicationView(CreateView):
    model = Application
    form_class = ContactUsForm
    template_name = 'jumanji/vacancy-detail.html'
    # success_url = reverse_lazy('application_send', self)
    pk = None

    def form_valid(self, form, *args, **kwargs):
        application = form.save(commit=False)
        vacancy = get_object_or_404(Vacancy, id=self.pk)
        application.user = self.request.user
        application.vacancy = vacancy
        print('ВАЖНЫЕ ДАННЫЕ')
        print(application.user)
        application.save()
        return redirect('application_send', self.pk)


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'jumanji/vacancy-detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = ContactUsForm
        return context


class VacancyApplicationView(View):
    def get(self, request, *args, **kwargs):
        view = VacancyDetailView.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CreateAapplicationView.as_view(*args, **kwargs)
        return view(request, *args, **kwargs)


class ApplicationSendView(View):
    template_name = 'jumanji/application-send.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SpecialtyVacanciesView(ListView):
    model = Vacancy
    template_name = template_name = 'jumanji/specialty.html'

    def get_queryset(self):
        specialty = self.kwargs['slug']
        queryset = Vacancy.objects.filter(specialty__code=specialty)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        specialty = Specialty.objects.filter(code=self.kwargs['slug'])
        context['title'] = specialty.first().title
        context['vacancies_count'] = self.get_queryset().count()
        return context


class CompanyView(ListView):
    model = Vacancy
    template_name ='jumanji/company.html'

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


class MyCompanyView(UpdateView):
    template_name = 'jumanji/mycompany/mycompany.html'
    model = Company
    form_class = CompanyForm
    success_url = reverse_lazy('mycompany')
    
    def get_object(self):
        user = self.request.user
        object = Company.objects.get(owner=user)
        return object

    def get(self, request):
        if not hasattr(request.user, 'company'):
            return redirect('letsstart_company')
        
        return super().get(request)


class StartCompanyView(View):
    template_name = 'jumanji/mycompany/letsstart.html'

    def get(self, request):
        return render(request, template_name=self.template_name)


class CreateCompanyView(CreateView):
    template_name = 'jumanji/mycompany/create-company.html'
    form_class = CompanyForm
    model = Company

    def form_valid(self, form):
        company = form.save(commit=False)
        company.owner = self.request.user
        company.save()
        return redirect('mycompany')


class MyCompanyVacanciesView(ListView):
    template_name = 'jumanji/mycompany/vacancies.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Vacancy.objects.filter(company__owner=user)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['has_vacancies'] = bool(user.company.vacancies.filter())
        return context


class CreateVacancyView(CreateView):
    template_name = 'jumanji/mycompany/vacancy-detail.html'
    form_class = VacancyForm
    model = Vacancy

    def form_valid(self, form):
        vacancy = form.save(commit=False)
        vacancy.company = self.request.user.company
        vacancy.save()
        return redirect('mycompany-vacancies')


class UpdateVacancyView(UpdateView):
    template_name = 'jumanji/mycompany/vacancy-detail.html'
    form_class = VacancyForm
    model = Vacancy

    def get_success_url(self):
        view_name =  'update_vacancy'
        return reverse(view_name, kwargs={'pk': self.object.id})


class MyResumeView(UpdateView):
    template_name = 'jumanji/myresume/myresume.html'
    form_class = ResumeForm
    model = Resume
    success_url = reverse_lazy('myresume')

    def get_object(self):
        user = self.request.user
        object = Resume.objects.get(user=user)
        return object

    def get(self, request):
        if not hasattr(request.user, 'resume'):
            return redirect('letsstart_resume')
        return super().get(request)


class LetsStartResumeView(View):
    template_name = 'jumanji/myresume/letsstart.html'

    def get(self, request):
        return render(request, self.template_name)


class CreateResumeView(CreateView):
    template_name = 'jumanji/myresume/create.html'
    form_class = ResumeForm
    model = Resume

    def form_valid(self, form):
        resume = form.save(commit=False)
        resume.user = self.request.user
        resume.save()
        return redirect('myresume')


class SearchPageView(ListView):
    model = Vacancy
    template_name = 'jumanji/vacancies.html'

    def get_queryset(self):
        query = self.request.GET.get('s')
        queryset = Vacancy.objects.filter(
            Q(title__icontains = query) | Q(description__icontains=query)
        )
        return queryset


def handler404(request, exception, template_name="404.html"):
    response = render(template_name)
    response.status_code = 404
    return response


def handler500(request, exception, template_name="500.html"):
    response = render(template_name)
    response.status_code = 500
    return response