from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User


class Project(models.Model):
    LOCATION_CHOICES = (
        ('on_campus', 'On Campus'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
    )

    title = models.CharField(max_length=200)
    professor = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    required_skills = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    compensation = models.TextField(blank=True)
    application_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Application(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    personal_statement = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
