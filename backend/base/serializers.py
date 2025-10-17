from rest_framework import serializers
from .models import Guest, Stay

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = "__all__"

class StaySerializer(serializers.ModelSerializer):
    guest = GuestSerializer(read_only=True)  # muestra el huésped como objeto
    guest_id = serializers.PrimaryKeyRelatedField(
        queryset=Guest.objects.all(), source="guest", write_only=True
    )
    guest_url = serializers.HyperlinkedRelatedField(
        view_name="guest-detail",  # usa el basename 'guest' del router
        read_only=True,
        lookup_field="pk"
    )

    class Meta:
        model = Stay
        fields = "__all__"