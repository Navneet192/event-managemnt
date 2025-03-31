from django.urls import path
from .views import create_event , events , book_event , update_event , delete_event
urlpatterns = [
    path('create_event/' , create_event , name='create_event'),
    path('events/' , events , name='events'),
    path('update_event/' , update_event , name='update_event'),
    path('delete_event/' , delete_event , name='delete_event'),
    path('book_event/' , book_event , name='book_event'),
]

