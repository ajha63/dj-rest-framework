from rest_framework import viewsets

from .serializers import DoctorSerializer
from .models import Doctor


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()