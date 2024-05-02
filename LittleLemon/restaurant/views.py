from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()  # Fetch all objects from the Booking model
    serializer_class = BookingSerializer  # Set the serializer class to BookingSerializer

#class UserViewSet(viewsets.ModelViewSet):
#   queryset = User.objects.all() 
#   serializer_class = UserSerializer
#   permission_classes = [permissions.IsAuthenticated] 