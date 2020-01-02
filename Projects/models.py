import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Developer")
    company = models.CharField(max_length=40)

    def __str__(self):
        return self.user.username

    def is_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.user.date_joined <= now

    is_published_recently.admin_order_field = 'user.date_joined'
    is_published_recently.boolean = True
    is_published_recently.short_description = 'Published recently?'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def is_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.user.date_joined <= now

    is_published_recently.admin_order_field = 'user.date_joined'
    is_published_recently.boolean = True
    is_published_recently.short_description = 'Published recently?'


class Project(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to='images')
    description = models.TextField(max_length=255)
    url = models.CharField(max_length=100)
    date = models.DateTimeField('published')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    developers = models.ManyToManyField(Developer, verbose_name="Related Developers")

    def __str__(self):
        return self.name

    def is_published_recently(self):
        now = timezone.now()
        return self.was_published_from() <= self.date <= now

    def inline_developers(self):
        return " , ".join([developer.user.username for developer in self.developers.all()])

    @staticmethod
    def was_published_from():
        return timezone.now() - datetime.timedelta(days=1)

    is_published_recently.admin_order_field = 'date'
    is_published_recently.boolean = True
    is_published_recently.short_description = 'Published recently?'
