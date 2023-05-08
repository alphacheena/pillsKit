from django.contrib import admin
from .models import Kit, Medicine


@admin.register(Kit)
class KitModelAdmin(admin.ModelAdmin):
    fields = ("user", "location")
    list_display = ("id", "user", "location")


@admin.register(Medicine)
class MedicineModelAdmin(admin.ModelAdmin):
    fields = ("kit", "name", "expire_date", "count")
    list_display = ("id", "kit", "name", "expire_date", "count")
