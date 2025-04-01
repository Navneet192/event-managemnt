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

          




