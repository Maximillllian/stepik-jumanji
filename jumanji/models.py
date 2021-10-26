import ast

from django.db import models
from django.utils import timezone


class Specialty(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    picture = models.URLField(default="https://place-hold.it/100x60")


class Company(models.Model):
    title = models.CharField(max_length=100)
    logo = models.URLField(default="https://place-hold.it/100x60")
    employee_count = models.IntegerField()
    description = models.TextField()


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    salary_from = models.IntegerField()
    salary_to = models.IntegerField()
    posted_at = models.DateField(default=timezone.now)
    skills = models.CharField(max_length=250)
    description = models.TextField()

    def get_skills(self):
        return self.skills.split(', ')