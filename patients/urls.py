from django.urls import path

from .views import list_patients, detail_patient

urlpatterns = [
    path('patients/', list_patients),
    path('patients/<int:pk>/', detail_patient),
]