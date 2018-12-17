from django.contrib import admin
from . import models


class TaskListAdmin(admin.ModelAdmin):
    list_display = ("title", )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "priority")


admin.site.register(models.Task, TaskListAdmin)
admin.site.register(models.Category, CategoryAdmin)