from django.urls import path
from .views import register , login , get_usersData
urlpatterns = [
   path('register/' , register, name='register'),
   path('login/' ,  login , name='login'),
   path('get_usersData/' , get_usersData , name='get_usersData')
]
