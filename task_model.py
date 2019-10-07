from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    code = models.IntegerField(default=0, blank=True, null=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    gender = models.IntegerField(default=1)
    role = models.IntegerField(default=1, blank=True, null=True)
    picture = models.TextField(blank=True, default="-", null=True)
    codedpicture = models.TextField(blank=True, default="-", null=True)
    class Meta:
        app_label = "task_service"

class Task(models.Model):
    parent_task = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, default="-", null=True)
    title = models.CharField(max_length=200)
    task_type = models.IntegerField(default=0)
    task_kind = models.IntegerField(default=0)
    create_date = models.DateField(auto_now_add=True)
    code = models.CharField(max_length=200, default='0')
    is_deleted = models.BooleanField(default=False)
    user_depends = models.ManyToManyField(User, blank=True, default="-")

    def natural_key(self):
        return (self.title)

    class Meta:
        unique_together = (('title'),)
        app_label = "task_service"

    def __str__(self):
        return self.title


class Activity(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    date = models.DateField()
    comment = models.TextField(verbose_name="activity descriptions")
    class Meta:
        app_label = "task_service"
    def __str__(self):
        return f'{self.task_id } - {self.user} - {self.date}'
