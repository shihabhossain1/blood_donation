from django.urls import path
from .views import *


urlpatterns = [
    path('', home,name='home'),
    path('sign_in/', signin, name='signin'),
    path('logout/', logout_view, name='logout')
    
]
