from rest_framework import serializers
from .models import Content
from courses.models import Course


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        exclude = ["course"]
        extra_kwargs = {
            "video_url": {"required": False},
        }

    def create(self, validated_data):
        course = self.context["view"].get_object()
        content = Content.objects.create(course=course, **validated_data)
        return content
