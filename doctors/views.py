from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import (
    Doctor,
    Department,
    DoctorAvailability,
    MedicalNote,
)
from .serializers import (
    DoctorSerializer,
    DepartmentSerializer,
    DoctorAvailabilitySerializer,
    MedicalNoteSerializer,
)

"""
GET  /api/doctors > List
POST /api/doctors > Create/Add
GET  /api/doctors/pk/ > one patient details
PUT /api/doctors/pk/ > one patient modify
DELETE /api/doctors/pk/ > one patient modify
""" 

class ListDoctorView(ListAPIView, CreateAPIView):
    """
    with the GET method displays a list of all doctors, 
    the POST method creates a new doctor.
    """

    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class DetailDoctorView(RetrieveUpdateDestroyAPIView):
    """
    With the GET method displays a doctor details, 
    the PUT method modify a doctor's record,
    the DELETE method deletes a doctor's record.
    """

    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()


class ListDepartmentView(ListAPIView, CreateAPIView):
    """
    with the GET method displays a list of Departments, 
    with the POST method creates a new department.
    """

    allowed_methods = ['GET', 'POST']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class DetailDepartmentView(RetrieveUpdateDestroyAPIView):
    """
    the GET method displays the details of a department, 
    the PUT method modify the data of a department,
    the DELETE method deletes a department's record.
    """
    
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class ListDoctorAvailabilityView(ListAPIView, CreateAPIView):
    """
    with the GET method displays all doctors availabilities, 
    the POST method creates a new doctor availability.
    """

    allowed_methods = ['GET', 'POST']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class DetailDoctorAvailabilityView(RetrieveUpdateDestroyAPIView):
    """
    With the GET method displays a doctor's availability details,
    the PUT method modifies the availability doctor details,
    the DELETE method delete a doctor's availabilities record.
    """
    
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = DoctorAvailabilitySerializer
    queryset = DoctorAvailability.objects.all()


class ListMedicalNoteView(ListAPIView, CreateAPIView):
    """
    with the GET method displays all medical notes, 
    the POST method creates a new medical note.
    """

    allowed_methods = ['GET', 'POST']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()


class DetailMedicalNoteView(RetrieveUpdateDestroyAPIView):
    """
    With the GET method displays a medical's notes details, 
    the PUT method modifies one medical notes details,
    the DELETE method delete a medical notes record.
    """
    
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = MedicalNoteSerializer
    queryset = MedicalNote.objects.all()
