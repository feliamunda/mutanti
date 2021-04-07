from django.contrib import admin

from .models import Human

# Register your models here to the admin.
@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    pass