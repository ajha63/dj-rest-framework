from django.urls import path

from .views import list_doctors, detail_doctor

urlpatterns = [
    path('doctors/', list_doctors),
    path('doctors/<int:pk>/', detail_doctor),
]