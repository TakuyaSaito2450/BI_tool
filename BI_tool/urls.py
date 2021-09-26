from django.urls import path
from .views import BI_tool
from . import views

urlpatterns = [
    path('a/', BI_tool),
    path('', views.IndexView.as_view(), name='index'),
    path('prefectures/<int:pk>', views.PrefecturesView.as_view(), name='prefectures'),
]
