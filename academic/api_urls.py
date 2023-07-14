from django.urls import path
from .api_views import (
    DepartmentAPIView,
    DepartmentDetailAPIView,
    CourseAPIView,
    CourseDetailAPIView,
    RoomAPIView,
    RoomDetailAPIView,
    ClassAPIView,
    ClassDetailAPIView,
    FieldAPIView,
    FieldDetailAPIView,
    SpecializationAPIView,
    SpecializationDetailAPIView,
)

urlpatterns = [
    path('departments/', DepartmentAPIView.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentDetailAPIView.as_view(), name='department-detail'),
    path('courses/', CourseAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('rooms/', RoomAPIView.as_view(), name='room-list'),
    path('rooms/<int:pk>/', RoomDetailAPIView.as_view(), name='room-detail'),
    path('classes/', ClassAPIView.as_view(), name='class-list'),
    path('classes/<int:pk>/', ClassDetailAPIView.as_view(), name='class-detail'),
    path('fields/', FieldAPIView.as_view(), name='field-list'),
    path('fields/<int:pk>/', FieldDetailAPIView.as_view(), name='field-detail'),
    path('specializations/', SpecializationAPIView.as_view(), name='specialization-list'),
    path('specializations/<int:pk>/', SpecializationDetailAPIView.as_view(), name='specialization-detail'),
]
