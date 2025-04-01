from django.db import models
class Booking(models.Model):
    user = models.ForeignKey('users.Users' , on_delete = models.CASCADE)
    events = models.ForeignKey('events.Events' , on_delete = models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    num_tickets = models.IntegerField((""))
    total_price = models.FloatField((""))
    payment_status = models.BooleanField(default = False)
    booking_status = models.BooleanField(default = False)

    def __str__ (self):
        return f"{self.user.first_name} - {self.events.event_name}"
