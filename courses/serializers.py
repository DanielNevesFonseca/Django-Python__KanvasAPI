from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "contents": {"read_only": True},
            "students": {"read_only": True},
            "instructor": {"required": False},
            "status": {"required": False},
            "students_courses": {"read_only": True},
        }
