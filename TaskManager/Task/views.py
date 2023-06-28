from rest_framework import generics,permissions

from .models import TaskTag,Tag,Task,TaskMeta
from .serializers import TaskTagSerializer,TagSerializer,TaskSerializer,TaskMetaSerializer
from .permissions import IsAuthorOrReadOnly

class TaskListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'Id'

class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'Id' 


class TaskTagListView(generics.ListCreateAPIView):
    queryset = TaskTag.objects.all()
    serializer_class = TaskTagSerializer

class TaskTagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskTag.objects.all()
    serializer_class = TaskTagSerializer
    lookup_field = 'Id'

class TaskMetaListView(generics.ListCreateAPIView):
    queryset = TaskMeta.objects.all()
    serializer_class = TaskMetaSerializer

class TaskMetaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskMeta.objects.all()
    serializer_class = TaskMetaSerializer
    lookup_field = 'Id'