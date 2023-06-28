from rest_framework import serializers
from .models import Task, TaskMeta, Tag, TaskTag


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'Id'
        model = Task
        fields = '__all__'
        read_only_fields = ('Id','id')


class TaskMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskMeta
        fields = ('Id','taskId','key','context')
        read_only_fields = ('Id','taskId')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('Id','title','slug')
        read_only_fields = ('Id','taskId')



class TaskTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTag
        fields = ('Id','taskId','tagId')
        read_only_fields = ('Id','taskId','tagId')
