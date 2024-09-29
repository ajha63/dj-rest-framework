from .serializers import PatientSerializer
from .models import Patient
from rest_framework.decorators import api_view 
from rest_framework.response import Response

@api_view(['GET'])
def list_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)