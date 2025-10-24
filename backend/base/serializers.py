from rest_framework import serializers

from .models import Guest, Stay


class GuestSerializer(serializers.ModelSerializer):
    last_stay = serializers.SerializerMethodField()
    class Meta:
        model = Guest
        fields = "__all__"

    def get_last_stay(self, obj):
        last_stay = obj.stays.order_by('-check_in').first()
        if last_stay:
            return {
                "id": last_stay.id,
                "check_in": last_stay.check_in,
                "check_out": last_stay.check_out
            }
        return None

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