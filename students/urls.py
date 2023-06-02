from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.studentlist, name='student_list'),
    
]