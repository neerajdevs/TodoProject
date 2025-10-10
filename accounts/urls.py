from django.urls import path , include
from .views import *

urlpatterns = [
    path('register' , register , name='register'),
    path('login' , login_view , name='login'),
    path('log_out' , log_out , name='log_out'),
    
]