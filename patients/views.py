from .serializers import PatientSerializer
from .models import Patient

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView


# GET  /api/patients > List
# POST /api/patients > Create/Add
# GET  /api/patients/pk/ > one patient details
# POST /api/patients/pk/ > one patient modify
# DELETE /api/patients/pk/ > one patient modify


class ListPatientsView(ListAPIView,CreateAPIView):
    allowed_methods = ['GET', 'POST']
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class DetailPatientView(APIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']

    def get(self, request, pk):
        try:
            patient = Patient.objects.get(id=pk)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            patient = Patient.objects.get(id=pk)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk):
        try:
            patient = Patient.objects.get(id=pk)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
