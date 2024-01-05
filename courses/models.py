from django.db import models
import uuid


class CourseStatus(models.TextChoices):
    NOT_STARTED = "not started"
    IN_PROGRESS = "in progress"
    FINISHED = "finished"


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    status = models.CharField(
        choices=CourseStatus.choices,
        default=CourseStatus.NOT_STARTED,
        max_length=11,
    )

    # Relationship with Account:Course -> 1:N
    instructor = models.ForeignKey(
        "accounts.Account",
        on_delete=models.SET_NULL,
        related_name="courses",
        null=True,
    )

    # Relationship with pivot table of Account:Course -> N:N
    students = models.ManyToManyField(
        "accounts.Account",
        through="students_courses.StudentCourse",
        related_name="my_courses",
    )

    def __str__(self) -> str:
        return f"{self.name} | {self.status}"
