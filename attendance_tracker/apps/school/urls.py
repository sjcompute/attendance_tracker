from django.urls import path
from . import views

urlpatterns = [
    path('school', views.SchoolView, name='school'),
    path('', views.SchoolView, name='school'),

]