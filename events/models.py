from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    organizer = models.CharField(max_length=100)
    rsvp = models.BooleanField(default=False)

    def __str__(self):
        return self.title

