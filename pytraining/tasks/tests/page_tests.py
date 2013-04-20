"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from tasks.models import Task, TaskHint


class TasksDisplayTest(TestCase):
    def setUp(self):
        self.tasks_url = reverse('tasks')
        self.user = User.objects.create(username='user',
                                        email='ilian@i-n-i.org',
                                        is_staff=True, is_active=True)
        task = Task(title='task-1', description='description-of-task-1',
                    created_by=self.user)
        task.save()

    def test_task_list_page(self):
        response =  self.client.get(self.tasks_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_list.html')
        for task in Task.objects.all():
            self.assertContains(response, task.title)

    def test_single_task_page(self):
        task = Task.objects.all()[0]
        url = reverse('single-task', kwargs={'slug': task.slug})
        response =  self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/single_task.html')
