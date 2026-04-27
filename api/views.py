from booking.models import Booking
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import BookingSerializer
from rest_framework import status

# Create your views here.
def register(request):
    pass

def account(request):
    pass

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def booking(request):
    if request.method == 'GET':
        bookings = Booking.objects.filter(booked_by=request.user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(booked_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
