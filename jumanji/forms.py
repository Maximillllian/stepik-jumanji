from django import forms
from .models import Company, Vacancy, Application, Resume


class CompanyForm(forms.ModelForm):

    class Meta:
        model =  Company
        exclude = ('owner',)


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        exclude = ('company', 'posted_at')


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = Application
        exclude = ('user', 'vacancy')


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        exclude = ('user',)