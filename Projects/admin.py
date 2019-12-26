# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Project


class ProjectInline(admin.TabularInline):
    model = Project.developers.through
    can_delete = False
    verbose_name_plural = 'Project'
    extra = 3


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['id', 'name']}),
        ('more Information', {'fields': ['date'], 'classes': ['collapse']})
    ]
    inlines = [ProjectInline]
    list_display = ('name', 'date', 'is_published_recently')
    list_filter = ['date']
    search_fields = ['name']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
