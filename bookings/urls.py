from django.urls import path
from .views import book_event
urlpatterns = [
    path('book_event/' , book_event , name='book_event')
]

