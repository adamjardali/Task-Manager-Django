from django.db import models
from utils.model_abstracts import CustomModel
from django.contrib.auth.models import User

class Task(CustomModel):
    class Status(models.TextChoices):
        PENDING = 'Pending'
        ACTIVE = 'Active'
        COMPLETED = 'Completed'

    userId = models.ForeignKey(User,on_delete=models.CASCADE,to_field='id') 
    title = models.CharField(max_length=512,default='New Task')
    description = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    hours = models.FloatField(default=0)
    planned_start_date = models.DateTimeField(null=True,blank=True)
    planned_end_date = models.DateTimeField(null=True,blank=True)
    actual_start_date = models.DateTimeField(null=True, blank=True)
    actual_end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Task {self.Id}'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class TaskMeta(CustomModel):
    taskId = models.ForeignKey(Task, on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    context = models.TextField(null=True)

    class Meta:
        verbose_name = 'TaskMeta'
        verbose_name_plural = 'TasksMeta'
        unique_together = ('key',)


class Tag(CustomModel):
    title = models.CharField(max_length=75,unique=True)
    slug = models.TextField(max_length=100)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class TaskTag(CustomModel):
    taskId = models.ForeignKey(Task, on_delete=models.CASCADE)
    tagId = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'TaskTag'
        verbose_name_plural = 'TasksTags'
        unique_together = ('taskId', 'tagId')



