from django.contrib import admin
from .models import Menu, Photo
# Импорт модели для доступа

admin.site.register(Menu)
# Подключение модели Menu к админке

@admin.register(Photo)
class MenuAdmin(admin.ModelAdmin):
    search_fields =['title']
    list_filter = ('menu',)
# Подключение модели Photo к админке