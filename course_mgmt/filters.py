import django_filters
from .models import Course, Enrollment


class CourseFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter(field_name="price", lookup_expr="exact")
    min_price = django_filters.NumberFilter(
        field_name="price", lookup_expr="gte", label="Min Price"
    )
    max_price = django_filters.NumberFilter(
        field_name="price", lookup_expr="lte", label="Max Price"
    )

    class Meta:
        model = Course
        fields = ["min_price", "max_price"]


class EnrollmentFilter(django_filters.FilterSet):
    user_id = django_filters.NumberFilter(
        field_name="user__id", lookup_expr="exact", label="User ID"
    )
    course_id = django_filters.NumberFilter(
        field_name="course__id", lookup_expr="exact", label="Course ID"
    )

    class Meta:
        model = Enrollment
        fields = ["user_id", "course_id"]
