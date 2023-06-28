from django.urls import path
from .views import TaskTagListView, TaskTagDetailView,TagListView,TagDetailView,TaskListView, TaskDetailView, TaskMetaListView, TaskMetaDetailView

urlpatterns = [
    path('tasktags/', TaskTagListView.as_view(), name='tasktag-list'),
    path('tasktags/<uuid:Id>/', TaskTagDetailView.as_view(), name='tasktag-detail'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<uuid:Id>/', TagDetailView.as_view(), name='tag-detail'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<uuid:Id>/', TaskDetailView.as_view(), name='task-detail'),
    path('task-meta/', TaskMetaListView.as_view(), name='task-meta-list'),
    path('task-meta/<uuid:Id>/', TaskMetaDetailView.as_view(), name='task-meta-detail'),
]
