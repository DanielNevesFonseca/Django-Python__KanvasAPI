from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from accounts.permissions import IsSuperUserPermission
from .models import Course
from .serializers import CourseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class ListCreateCourseView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserPermission, IsAuthenticated]


class RetrieveUpdateDestroyCourseView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"
