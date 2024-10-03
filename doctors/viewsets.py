from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import DoctorSerializer
from .models import Doctor


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    @action(['POST'], detail=True, url_path='vacation-set-on')
    def set_on_vacation(self, requests, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = True
        doctor.save()
        return Response({"status": "The doctor is on vacation"})

    @action(['POST'], detail=True, url_path='vacation-set-off')
    def set_off_vacation(self, requests, pk):
        doctor = self.get_object()
        doctor.is_on_vacation = False
        doctor.save()
        return Response({"status": "The doctor is not on vacations"})
    
