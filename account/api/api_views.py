from rest_framework.generics import CreateAPIView
from .serialisers import UserSerialiser
from ..models import CustomUser


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerialiser

    def perform_create(self, serializer):
        user = serializer.validated_data
        CustomUser.objects.create_user(user["email"], user["password"])

