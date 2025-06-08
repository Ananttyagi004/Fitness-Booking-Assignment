from django.urls import path
from .views import ClassListAPIView, BookingCreateAPIView, BookingListAPIView

urlpatterns = [
    path('classes/', ClassListAPIView.as_view(), name='class-list'),
    path('book/', BookingCreateAPIView.as_view(), name='book-class'),
    path('bookings/', BookingListAPIView.as_view(), name='booking-list'),
]
