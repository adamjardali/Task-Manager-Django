from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Task, TaskMeta, Tag, TaskTag
from .serializers import TaskSerializer, TaskMetaSerializer, TagSerializer, TaskTagSerializer


class TaskModelTest(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.task = Task.objects.create(title='Sample Task')
        self.task_meta = TaskMeta.objects.create(taskId=self.task, key='sample_key')

    def test_task_model(self):
        # Test the Task model's __str__() method
        self.assertEqual(str(self.task), 'Task {}'.format(self.task.Id))

    def test_task_serializer(self):
        # Test the TaskSerializer
        serializer = TaskSerializer(instance=self.task)
        data = serializer.data

        # Add your assertions for the serializer's fields here
        self.assertEqual(data['title'], 'Sample Task')

    def test_task_meta_serializer(self):
        # Test the TaskMetaSerializer
        serializer = TaskMetaSerializer(instance=self.task_meta)
        data = serializer.data

        # Add your assertions for the serializer's fields here
        self.assertEqual(data['key'], 'sample_key')


class TaskAPITest(APITestCase):
    def setUp(self):
        # Create sample data for testing
        self.task = Task.objects.create(title='Sample Task')
        self.tag = Tag.objects.create(title='Sample Tag', slug='sample-tag')
        self.task_tag = TaskTag.objects.create(taskId=self.task, tagId=self.tag)

    def test_task_list_view(self):
        # Test the TaskListView
        response = self.client.get('/tasks/')  # Replace '/tasks/' with the actual URL for the task list view

        # Add your assertions for the response here
        self.assertEqual(response.status_code, 200)

    def test_task_detail_view(self):
        # Test the TaskDetailView
        response = self.client.get('/tasks/{}/'.format(self.task.Id))  # Replace '/tasks/{}/' with the actual URL for the task detail view

        # Add your assertions for the response here
        self.assertEqual(response.status_code, 200)

    # Add similar test methods for other views (TagListView, TagDetailView, TaskTagListView, TaskTagDetailView, TaskMetaListView, TaskMetaDetailView)
