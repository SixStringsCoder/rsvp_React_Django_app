from rsvpapp.models import Guest
from rsvpapp.serializers import GuestSerializer
from rest_framework import generics

# Create your views here.

class GuestListCreate(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer