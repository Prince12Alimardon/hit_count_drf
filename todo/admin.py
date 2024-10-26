from django.contrib import admin
from hitcount.models import HitCount
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')


admin.site.register(Todo, TodoAdmin)
# admin.site.register(HitCount)  # Register the HitCount model for tracking hits
