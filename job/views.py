from django.http import Http404
from django.shortcuts import render
from django.views import View

from job.models import Company
from job.models import Specialty
from job.models import Vacancy


class MainView(View):
    def get(self, request):
        return render(
            request, 'index.html', {
                'specialities': Specialty.objects.all(),
                'companies': Company.objects.all()
            }
        )


class VacanciesView(View):
    def get(self, request, ):
        return render(
            request, 'list.html', {
                'vacancies': Vacancy.objects.all(),
                'count_vacancies': Vacancy.objects.count()
            }
        )


class VacancyView(View):
    def get(self, request, id: int):
        if not Vacancy.objects.filter(id=id):
            raise Http404('Страница не найдена')

        return render(
            request, 'vacancy.html', {
                'vacancy': Vacancy.objects.filter(id=id).first()
            }
        )


class SendView(View):
    def get(self, request, id: int):
        return render(
            request, 'sent.html',
        )


class SpecializationView(View):
    def get(self, request, specialization: str):
        if not Specialty.objects.filter(code=specialization):
            raise Http404('Страница не найдена')

        return render(
            request, 'list.html', {
                'vacancies': Vacancy.objects.filter(specialty__code=specialization),
                'count_vacancies': Vacancy.objects.filter(specialty__code=specialization).count(),
                'speciality_title': Specialty.objects.filter(code=specialization).first()
            }
        )


class CompaniesView(View):
    def get(self, request, ):
        return render(
            request, 'list.html',
        )


class CompanyView(View):
    def get(self, request, id: int):
        if not Company.objects.filter(id=id):
            raise Http404('Страница не найдена')

        return render(
            request, 'company.html', {
                'company': Company.objects.filter(id=id).first(),
                'vacancies': Vacancy.objects.filter(company__id=id),
            }
        )
