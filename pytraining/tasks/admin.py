from django.contrib import admin

from tasks.models import Task, TaskHint


class TaskHintInline(admin.TabularInline):
    model = TaskHint


class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskHintInline]
admin.site.register(Task, TaskAdmin)


admin.site.register(TaskHint)