import sys
sys.path.append('..')

from jumanji.models import Company, Specialty, Vacancy

from data import jobs, companies, specialties


for company in companies:
    new_company = Company(
        title=company['title'],
        logo=company['logo'],
        employee_count = company['employee_count'],
        description = company['description']
    )
    new_company.save()

for specialty in specialties:
    new_specialty = Specialty(
        code=specialty['code'],
        title=specialty['title']
    )
    new_specialty.save()


for job in jobs:
    company = Company.objects.filter(id=job['id'])[0]
    specialty = Specialty.objects.filter(code=job['specialty'])[0]

    vacancy = Vacancy(
        title=job['title'],
        specialty=specialty,
        company=company,
        salary_from=job['salary_from'],
        salary_to=job['salary_to'],
        posted_at=job['posted'],
        skills=job['skills'],
        description=job['description']
    )
    vacancy.save()