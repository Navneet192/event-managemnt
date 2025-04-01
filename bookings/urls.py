from django.urls import path
from .views import book_event , bookings
urlpatterns = [
    path('book_event/' , book_event , name='book_event'),
    path('bookings/' , bookings , name='bookings'),
    path('bookings/<str:event_location>/' , bookings , name='booking_by_location'),
]

