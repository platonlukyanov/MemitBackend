from django.contrib import admin
from .models import EdCard


@admin.register(EdCard)
class ContactTypeAdmin(admin.ModelAdmin):
    list_display = ('term', 'answer', 'created', 'user')
