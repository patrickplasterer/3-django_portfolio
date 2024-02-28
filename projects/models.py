from django.db import models
from django.utils import timezone

PROJECT_STATUS_CHOICES = (
    ("I", "Incomplete"),
    ("C", "Complete"),
)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateField(default=timezone.now())
    technology = models.CharField(max_length=20)
    status = models.CharField(max_length=1, choices=PROJECT_STATUS_CHOICES, default="I")
    image = models.FileField(upload_to="project_images/", blank=True)

    def __str__(self):
        return self.title
