# Generated by Django 3.2.8 on 2021-10-25 10:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('logo', models.URLField(default='https://place-hold.it/100x60')),
                ('employee_count', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('picture', models.URLField(default='https://place-hold.it/100x60')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('salary_from', models.IntegerField()),
                ('salary_to', models.IntegerField()),
                ('posted_at', models.DateField(default=django.utils.timezone.now)),
                ('skills', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='jumanji.company')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='jumanji.speciality')),
            ],
        ),
    ]