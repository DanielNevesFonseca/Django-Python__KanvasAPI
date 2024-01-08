from rest_framework import serializers
from accounts.models import Account
from courses.models import Course

from students_courses.models import StudentCourse


class StudentsCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = ["id", "student_id", "student_username", "student_email", "status"]
        extra_kwargs = {"id": {"read_only": True}}

    student_id = serializers.CharField(source="student.id", read_only=True)
    student_username = serializers.CharField(source="student.username", read_only=True)
    student_email = serializers.CharField(source="student.email")


class CourseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]
        read_only_fields = ["name"]

    students_courses = StudentsCoursesSerializer(many=True)

    def update(self, instance, validated_data):
        found_students_list = []
        not_found_students_list = []

        for user_raw in validated_data["students_courses"]:
            student = user_raw["student"]
            account = Account.objects.filter(email=student["email"]).first()
            if not account:
                not_found_students_list.append(student["email"])
            else:
                found_students_list.append(account)

        if not_found_students_list:
            raise serializers.ValidationError(
                {"detail": f"No active accounts was found: {", ".join(not_found_students_list)}."}
            )
        instance.students.add(*found_students_list)

        return instance
