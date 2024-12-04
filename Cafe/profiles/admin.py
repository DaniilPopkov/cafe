from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class profilesAdmin(admin.ModelAdmin):
    list_display=(
        'user', 'first_name', 'last_name', 'patronimic'
    )
# Подключение модели Profile к админке