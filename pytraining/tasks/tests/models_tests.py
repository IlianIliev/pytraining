"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User

from tasks.models import Task, TaskHint


class TasksModelsTest(TestCase):
    def setUp(self):
         self.user = User.objects.create(username='user',
                                         email='ilian@i-n-i.org',
                                         is_staff=True, is_active=True)

    def test_task_and_hint_creation(self):
        task = Task(title='Task 1',
                    description='Description of task 1',
                    created_by=self.user)
        task.save()
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(task.slug, 'task-1')

        hint = TaskHint(task=task, created_by=self.user,
                        hint='This is hint 1 for taks 1')
        hint.save()
        self.assertEqual(TaskHint.objects.count(), 1)
        self.assertEqual(hint.position, 1)
        
        hint2 = TaskHint(task=task, created_by=self.user,
                        hint='This is hint 2 for taks 1')
        hint2.save()
        self.assertEqual(TaskHint.objects.count(), 2)
        self.assertEqual(hint2.position, 2)
