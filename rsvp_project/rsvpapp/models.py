from django.db import models

# Create your models here.

class Guest(models.Model):
    """ Model for Guest to be added to RSVP list"""

    guest_name = models.CharField(max_length=30, help_text="Enter Guest Name")
    is_confirmed = models.BooleanField(default=False)


    def __str__(self):
        """Represents model object as Guest name in Admin area"""
        return self.guest_name
