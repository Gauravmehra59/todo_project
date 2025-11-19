from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "due_date", "status")
    search_fields = ("title", "status")
    list_filter = ("status",)
