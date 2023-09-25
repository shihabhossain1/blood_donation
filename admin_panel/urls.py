from django.urls import path
from .views import *


urlpatterns = [
    path('customers', home,name='home')
]
