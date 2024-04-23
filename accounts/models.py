from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Additional fields
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    twitter_link = models.URLField(max_length=200, blank=True)
    facebook_link = models.URLField(max_length=200, blank=True)
    linkedin_link = models.URLField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # Specify unique related names for the reverse relationships
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username
