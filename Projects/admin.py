# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Project, Developer, Customer


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']})
    ]


@admin.register(Customer)
class DeveloperAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']})
    ]


class DeveloperInline(admin.TabularInline):
    model = Project.developers.through
    can_delete = False
    verbose_name_plural = 'Developer'
    extra = 2


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'customer', 'image']}),
        ('more Information', {'fields': ['date'], 'classes': ['collapse']})
    ]
    inlines = [DeveloperInline]
    list_display = ('name', 'date', 'is_published_recently')
    list_filter = ['date']
    search_fields = ['name']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
