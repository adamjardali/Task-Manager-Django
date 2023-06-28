from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from utils.model_abstracts import CustomModel


# class Profile(CustomModel):
#     class Role(models.TextChoices):
#         ADMIN = 'Admin'
#         VIEWER = 'Viewer'

#     _user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
#     role = models.CharField(max_length=20, choices=Role.choices, default=Role.ADMIN)
#     firstName = models.CharField(max_length=255)
#     middleName = models.CharField(max_length=255, null=True,blank=True)
#     lastName = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255, unique=True)
#     bio = models.TextField(blank=True, null=True)
#     countryCode = models.CharField(max_length=25)
#     phone = models.CharField(max_length=25)
#     profilePicture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
#     lastLogin = models.DateTimeField(default=timezone.now,blank=True)

#     def __str__(self):
#         return f'{firstName} {lastName}'
        
#     class Meta:
#         verbose_name = 'Profile'
#         verbose_name_plural = 'Profiles'


class Activity(CustomModel):
    class Status(models.TextChoices):
        ADDTASK = 'ADDTASK'
        DELETETASK = 'DELETETASK'
        UPDATETASK = 'UPDATETASK'
        GETTASK = 'GETTASK'

    userId = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')
    taskId = models.ForeignKey('Task.Task', on_delete=models.CASCADE, to_field='Id')
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=2048)
    status = models.CharField(max_length=20, choices=Status.choices)
    hours = models.FloatField(default=0)
    plannedStartDate = models.DateTimeField(null=True, blank=True)
    plannedEndDate = models.DateTimeField(null=True, blank=True)
    actualStartDate = models.DateTimeField(null=True, blank=True)
    actualEndDate = models.DateTimeField(null=True, blank=True)
    context = models.TextField()

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
        unique_together = ('userId', 'taskId')


class Comment(CustomModel):
    taskId = models.ForeignKey('Task.Task', on_delete=models.CASCADE, to_field='Id')
    activityId = models.ForeignKey(Activity, on_delete=models.CASCADE, to_field='Id')
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        unique_together = ('taskId', 'activityId')

