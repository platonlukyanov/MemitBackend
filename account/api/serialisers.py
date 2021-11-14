from rest_framework import serializers

from ..models import CustomUser


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "password"]
        write_only_fields = ["password"]
