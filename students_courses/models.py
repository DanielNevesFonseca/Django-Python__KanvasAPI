from django.db import models
import uuid


class StudentCourseStatus(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"


class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(
        null=False,
        choices=StudentCourseStatus.choices,
        default=StudentCourseStatus.PENDING,
        max_length=50,
    )

    # Tabela pivô customizada...
    student = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="students_courses",
        null=False,
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="students_courses",
        null=False,
    )
