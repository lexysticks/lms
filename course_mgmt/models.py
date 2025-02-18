from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    course = models.ForeignKey(
        to=Course, related_name="enrollments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=User, related_name="enrollments", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.course.title} - {self.user.email}"
