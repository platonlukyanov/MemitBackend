from django.db import models
from django.conf import settings


class EdCard(models.Model):
    """Модель карточек для изучения"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="edcards")
    term = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
