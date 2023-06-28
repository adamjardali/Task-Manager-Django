from django.contrib import admin
from .models import Task, TaskMeta, Tag, TaskTag
# Register your models here.

admin.site.register(Task)
admin.site.register(TaskMeta)
admin.site.register(Tag)
admin.site.register(TaskTag)