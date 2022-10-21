from django.urls import include, path

from rest_framework import routers


from .views import TeacherView
from .views import ClassesView

router = routers.DefaultRouter()
router.register(r'teacher', TeacherView)

router.register(r'classes', ClassesView)



urlpatterns = [
   path('', include(router.urls)),
]