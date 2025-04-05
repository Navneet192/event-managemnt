from rest_framework.routers import DefaultRouter
from .views import EventsViewSet
router = DefaultRouter()
router.register(r'events' , EventsViewSet , basename='events')
urlpatterns = router.urls

