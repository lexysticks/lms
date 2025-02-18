from django.urls import path
from .views import CourseViewSet, EnrollmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"courses", CourseViewSet)
router.register(r"enrollments", EnrollmentViewSet)

urlpatterns = router.urls
