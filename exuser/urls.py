from django.urls import path
from exuser.views import *

urlpatterns = [
    path('employee/', employee, name='employee'),
    path('addemployee/', addemployee, name='addemployee'),
]
