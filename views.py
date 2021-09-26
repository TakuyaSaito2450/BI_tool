from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from .models import Littering, Prefectures


# Create your views here.


def BI_tool(request):
    return HttpResponse('')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        littering_list = Littering.objects.all().order_by('prefectures')
        params = {'littering_list': littering_list, }
        return params


class PrefecturesView(DetailView):
    model = Prefectures

    def get_context_data(self, **kwargs):
        prefectures_name = kwargs['object'].name
        littering_list = Littering.objects.filter(prefectures=kwargs['object']).order_by('-collection_date')[:3]
        params = {
            'prefectures_name': prefectures_name,
            'littering_list': littering_list,
        }
        return params
