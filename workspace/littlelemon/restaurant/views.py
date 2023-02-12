from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu
from rest_framework import generics
from .serializers import MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    model = Menu
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pass

class SingleItemMenuView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer