from django.urls import path
from . import views

urlpatterns = [
    path('teacher', views.TeacherView, name='teacher'),
    path('', views.TeacherView, name='teacher'),

]