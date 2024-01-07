from rest_framework import serializers
from .models import StudentCourse


class StudentsCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = "__all__"