from django.db import models

class Events(models.Model):
    event_name = models.CharField(max_length = 250)
    event_discription = models.CharField(max_length = 300)
    event_category = models.CharField(max_length = 250)
    event_date = models.DateField((""))
    event_time = models.IntegerField((""))
    event_capacity = models.IntegerField((""))
    event_price = models.FloatField((""))
    event_location = models.CharField(max_length = 250)

    def __str__(self):
        return self.event_name 
    
class Booking(models.Model):
    user = models.ForeignKey('users.Users' , on_delete = models.CASCADE)
    events = models.ForeignKey('events.Events' , on_delete = models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    num_tickets = models.IntegerField((""))
    total_price = models.FloatField((""))
    payment_status = models.BooleanField(('default = False'))
    booking_status = models.BooleanField(('default = False'))

    def __str__ (self):
        return f"{self.user_name} - {self.events.event_name}"

class Ticket(models.Model):
    ticket_id = models.CharField(max_length = 250 , unique = True)
    booking = models.ForeignKey('events.Booking' , on_delete = models.CASCADE)
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.ticket_id
          




