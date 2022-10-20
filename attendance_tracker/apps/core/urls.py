from django.urls import include, path

from rest_framework import routers

from .views import SchoolView

router = routers.DefaultRouter()
router.register(r'school', SchoolView)


urlpatterns = [
   path('', include(router.urls)),
]