from django.urls import include, path

from rest_framework import routers

from .views import SchoolView
from .views import TeacherView

router = routers.DefaultRouter()
router.register(r'school', SchoolView)
router.register(r'teacher', TeacherView)


urlpatterns = [
   path('', include(router.urls)),
]