from django.utils import timezone
from django.views import generic

from .models import Project


class IndexView(generic.ListView):
    model = Project
    template_name = 'Projects/index.html'

    def get_queryset(self):
        """
        Excludes any Project that aren't published yet.
        """
        return Project.objects.filter(date__lte=timezone.now()).order_by('date')


class DetailsView(generic.DetailView):
    model = Project
    template_name = 'Projects/details.html'
