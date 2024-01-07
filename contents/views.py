from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import NotFound

from courses.models import Course
from .models import Content
from .serializers import ContentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsSuperUserPermission, IsCourseParticipantPermission


class CreateContentView(CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    # lookup_url_kwarg = "course_id"

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserPermission]

    def get_object(self):
        course_id = self.kwargs["course_id"]
        course = get_object_or_404(Course, id=course_id)
        return course


class RetrieveUpdateDestroyContentView(RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "content_id"

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserPermission, IsCourseParticipantPermission]

    def get_object(self):
        content = Content.objects.filter(id=self.kwargs["content_id"]).first()
        course = Course.objects.filter(pk=self.kwargs["course_id"]).first()
        if not content:
            raise NotFound({"detail": "content not found."})
        if not course:
            raise NotFound({"detail": "course not found."})
        return content