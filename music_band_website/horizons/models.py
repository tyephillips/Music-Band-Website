from django.db import models


# Create your models here.
class Event(models.Model):
    """
    Represents an event for the band, including details like name, date,
    time, location, ticket price, and a description.
    """
    # Name of the event.
    name = models.CharField(max_length=100)
    # Date of the event.
    date = models.DateField()
    # Time of the event.
    time = models.TimeField()
    # Location of the event.
    location = models.CharField(max_length=200)
    # Ticket price for the event.
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Description of the event.
    description = models.TextField()

    def __str__(self):
        """
        Returns the name of the event as its string representation.
        """
        return self.name