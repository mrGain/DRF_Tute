from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# REgester Student Viewset with router

router.register("student", views.StudentViewSet, basename="student")

urlpatterns = [
    path('',include(router.urls))
]

