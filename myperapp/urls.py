from django.urls import path,include
from .views import *
urlpatterns = [
  path('',home,name='home'),
  path('ex/',ex,name='hex'),
  path('projects/',projects,name="projects"),
]