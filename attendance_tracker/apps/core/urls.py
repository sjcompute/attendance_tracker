from django.urls import include, path

from rest_framework import routers


from .views import TeacherView
from .views import ClassesView
from .views import AttendanceView
from .views import StudentView
router = routers.DefaultRouter()
router.register(r'teacher', TeacherView)
router.register(r'attendance', AttendanceView)
router.register(r'classes', ClassesView)
router.register(r'student', StudentView)


urlpatterns = [
   path('', include(router.urls)),
]