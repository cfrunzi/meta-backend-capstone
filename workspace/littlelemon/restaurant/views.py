from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu, Booking
from rest_framework import generics
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    model = Menu
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleItemMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingView(generics.ListCreateAPIView):
    model = Booking
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleBookingItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer