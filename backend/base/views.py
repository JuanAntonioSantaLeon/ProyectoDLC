from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Guest, Stay
from .serializers import GuestSerializer, StaySerializer

class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all().order_by("last_name")
    serializer_class = GuestSerializer

class StayViewSet(viewsets.ModelViewSet):
    serializer_class = StaySerializer

    def get_queryset(self):
        queryset = Stay.objects.all().select_related("guest")
        guest_id = self.kwargs.get("guest_pk")  # viene del nested router
        if guest_id:
            queryset = queryset.filter(guest_id=guest_id)
        return queryset

    def perform_create(self, serializer):
        guest_id = self.kwargs.get("guest_pk")
        if guest_id:
            guest = Guest.objects.get(pk=guest_id)
            serializer.save(guest=guest)
        else:
            serializer.save()