from django.db import models
class Booking(models.Model):
    event_id = models.IntegerField(default=0)
    contact_email = models.EmailField(default="")
    contact_phone = models.CharField(max_length=15 , default="")
    num_tickets = models.IntegerField((""))
    def __str__ (self):
        return f"{self.user.first_name} - {self.events.event_name}"
    
    
