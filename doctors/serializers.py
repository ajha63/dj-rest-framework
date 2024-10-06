from datetime import date
from rest_framework import serializers

from .models import Doctor, Department, DoctorAvailability, MedicalNote


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_email(self, value):
        if "@plainsboroteaching.care" in value:
            return value
        raise serializers.ValidationError("Solo correos del dominio @plainsboroteaching.care son permitidos")

    def validate(self, attrs):
        if len(attrs['contact_number']) < 10 and attrs['is_on_vacation']:
            raise serializers.ValidationError(
                "Por favor, ingrese un número válido antes de irte a vacaciones"
            )
        return super().validate(attrs)


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    experience = serializers.SerializerMethodField()

    class Meta:
        model = DoctorAvailability
        fields = [
            'doctor',
            'experience',
            'start_date',
            'end_date',
            'start_time',
            'end_time',
        ]

    def get_experience(self, obj):
        """
        Return the doctor experience in years
        """

        # get age in days (timedelta)
        experience_timedelta = date.today() - obj.start_date
        years = experience_timedelta.days // 365
        return f"{years}"


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = '__all__'
