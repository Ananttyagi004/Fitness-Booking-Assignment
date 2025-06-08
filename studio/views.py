from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import localtime
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer, BookingCreateSerializer

class ClassListAPIView(APIView):
    def get(self, request):
        classes = FitnessClass.objects.filter(date_time__gte=localtime()).order_by('date_time')
        serializer = FitnessClassSerializer(classes, many=True)
        return Response(serializer.data)

class BookingCreateAPIView(APIView):
    def post(self, request):
        serializer = BookingCreateSerializer(data=request.data)
        if serializer.is_valid():
            class_id = serializer.validated_data['class_id']
            try:
                fitness_class = FitnessClass.objects.get(id=class_id)
            except FitnessClass.DoesNotExist:
                return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)

            if fitness_class.available_slots <= 0:
                return Response({"error": "No slots available"}, status=status.HTTP_400_BAD_REQUEST)

            booking = Booking.objects.create(
                fitness_class=fitness_class,
                client_name=serializer.validated_data['client_name'],
                client_email=serializer.validated_data['client_email']
            )
            fitness_class.available_slots -= 1
            fitness_class.save()
            return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingListAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        bookings = Booking.objects.filter(client_email=email)
        return Response(BookingSerializer(bookings, many=True).data)

