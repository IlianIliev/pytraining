from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max

from django_autoslug.fields import AutoSlugField


class CreatedBy(models.Model):
    """ Abstract class that adds field for the user created the object, the
    datetime of the creation and the datetime of the last update """
    created_by = models.ForeignKey(User, related_name='%(class)ss')
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Task(CreatedBy):
    """ Model for tasks """
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField()

    class Meta:
        ordering = ('-created_at', )

    def __unicode__(self):
        return self.title


class TaskHint(CreatedBy):
    """ Model for task hints """ 
    task = models.ForeignKey(Task, related_name='hints')
    hint = models.CharField(max_length=255)
    position = models.PositiveSmallIntegerField()

    def save(self, *args, **kwargs):
        """ Autopopulates the position filed will the next bigger value """
        if not self.position:
            max = TaskHint.objects.filter(task=self.task).aggregate(
                                                            Max('position'))
            self.position = (max['position__max'] or 0) + 1
        super(TaskHint, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.hint


class TaskProposal(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    text = models.TextField()

    def __unicode__(self):
        return self.text
