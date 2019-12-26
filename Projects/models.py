import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Developer(models.Model):
    user = models.OneToOneField(User)
    company = models.CharField(max_length=40)

    def __str__(self):
        return self.user.username

    def is_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.user.date_joined <= now

    is_published_recently.admin_order_field = 'date'
    is_published_recently.boolean = True
    is_published_recently.short_description = 'Published recently?'


class Customer(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

    def is_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.user.date_joined <= now

    is_published_recently.admin_order_field = 'date'
    is_published_recently.boolean = True
    is_published_recently.short_description = 'Published recently?'


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    date = models.DateTimeField('published')
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    developers = models.ManyToManyField(Developer)

    def __str__(self):
        return self.name

    def is_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now

    is_published_recently.admin_order_field = 'date'
    is_published_recently.boolean = True
    is_published_recently.short_description = 'Published recently?'


class Plugin(models.Model):
    plugin_id = models.AutoField(primary_key=True)
    project = models.ManyToManyField(Project, through='Project')
    name = models.CharField(max_length=60)
    date = models.DateTimeField('published')

    def __str__(self):
        return self.name

    def is_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now

    is_published_recently.admin_order_field = 'date'
    is_published_recently.boolean = True
    is_published_recently.short_description = 'Published recently?'
