from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('professor', 'Professor'),
        ('student', 'Student'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    bio = models.TextField(max_length=500, blank=True)
    research_interests = models.TextField(max_length=1000, blank=True)
    skills = models.TextField(max_length=500, blank=True)
    department = models.CharField(max_length=100, blank=True)
