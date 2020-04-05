from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    employee_count = models.IntegerField()


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=256)
    logo = models.CharField(max_length=256)


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

# class  Response(models.Model):
# title = models.CharField(max_length=64)
# username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_response')
# tel = models.IntegerField()
# description = models.CharField(max_length=1024)
# vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vacancy_response')
