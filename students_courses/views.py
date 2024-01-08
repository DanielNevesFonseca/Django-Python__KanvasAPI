from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import status
from accounts.permissions import IsSuperUserPermission
from courses.models import Course
from students_courses.models import StudentCourse, StudentCourseStatus
from .serializers import CourseStudentSerializer


class RetrieveUpdateStudentsInCourseView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserPermission]

    queryset = Course.objects.all()
    serializer_class = CourseStudentSerializer
    lookup_url_kwarg = "course_id"
