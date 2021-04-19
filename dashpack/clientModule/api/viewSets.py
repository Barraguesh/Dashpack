#Python/Django
from rest_framework.permissions import IsAdminUser
from django.http import HttpResponse
from rest_framework import viewsets

#Models
from clientModule.models import Client
from clientModule.models import Device
from clientModule.models import Ticket

#Serializers
from clientModule.api.serializers import ClientSerializer
from clientModule.api.serializers import DeviceSerializer
from clientModule.api.serializers import TicketSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser]

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAdminUser]

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAdminUser]