from django.db import models
import uuid


class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, null=False)
    content = models.TextField(null=False)
    video_url = models.CharField(max_length=200, null=False)

    # Relationship of Content:Course -> N:1
    course = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE, related_name="contents"
    )
