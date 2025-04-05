from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import bookingViewSet
router = DefaultRouter()
router.register(r'booking' , bookingViewSet , basename='booking')

urlpatterns = [
    path('api/' , include(router.urls)),
    # path('bookings/' , bookings , name='bookings'),
    # path('bookings/<str:event_location>/' , bookings , name='booking_by_location'),
]



