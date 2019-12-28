from django.utils import timezone
from django.views import generic

from .models import Project


class IndexView(generic.ListView):
    model = Project
    template_name = 'Projects/index.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Project.objects.filter(date__lte=timezone.now())
