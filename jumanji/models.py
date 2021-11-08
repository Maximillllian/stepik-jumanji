from phonenumber_field.modelfields import PhoneNumberField

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Specialty(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="specialty_logos", default="https://place-hold.it/100x60")

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to="company_logos", default="https://place-hold.it/100x60")
    employee_count = models.IntegerField()
    description = models.TextField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="company", blank=True, null=True)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies", default=None)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    salary_from = models.IntegerField()
    salary_to = models.IntegerField()
    posted_at = models.DateField(default=timezone.now)
    skills = models.CharField(max_length=250)
    description = models.TextField()

    def get_skills(self):
        return self.skills.split(', ')
    
    def __str__(self):
        return self.title


class Application(models.Model):
    name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    message = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications", default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")

    def __str__(self):
        return self.name


class Resume(models.Model):

    class Status(models.TextChoices):
        NOT_LOOKING = 'NOT', 'Не ищу работу'
        CONSIDERING = 'CONS', 'Рассматриваю предложения'
        LOOKING = 'LOOK', 'Ищу работу'

    class Grade(models.TextChoices):
        TRAINEE = 'TR', 'Стажер'
        JUNIOR = 'JUN', 'Джуниор'
        MIDDLE = 'MID', 'Миддл'
        SENIOR = 'SEN', 'Сеньор'
        LEAD = 'LEAD', 'Лид'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="resume")
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    status = models.CharField(max_length=4, choices=Status.choices, default=Status.LOOKING)
    salary = models.IntegerField()
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="resumes")
    grade = models.CharField(max_length=4, choices=Grade.choices, default=Grade.MIDDLE)
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.URLField()