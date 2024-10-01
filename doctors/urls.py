from django.urls import path

from .views import (
    ListDoctorView,
    DetailDoctorView,
    ListDepartmentView,
    DetailDepartmentView,
    ListDoctorAvailabilityView,
    DetailDoctorAvailabilityView,
    ListMedicalNoteView,
    DetailMedicalNoteView,
)

urlpatterns = [
    path('doctors/', ListDoctorView.as_view()),
    path('doctors/<int:pk>/', DetailDoctorView.as_view()),
    path('departments/', ListDepartmentView.as_view()),
    path('departments/<int:pk>/', DetailDepartmentView.as_view()),
    path('doctoravailabilities/', ListDoctorAvailabilityView.as_view()),
    path('doctoravailabilities/<int:pk>/', DetailDoctorAvailabilityView.as_view()),
    path('medicalnotes/', ListMedicalNoteView.as_view()),
    path('medicalnotes/<int:pk>/', DetailMedicalNoteView.as_view()),
]