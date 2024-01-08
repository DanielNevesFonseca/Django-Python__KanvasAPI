from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Course
from .serializers import CourseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsSuperUserOrReadOnlyPermission, IsSuperUserPermission


class ListCreateCourseView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserOrReadOnlyPermission]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Course.objects.all()

        return Course.objects.filter(students=self.request.user)


class RetrieveUpdateDestroyCourseView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserPermission]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"
