from django.urls import path

from . import views

app_name = 'Projects'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('project/<int:pk>', views.DetailsView.as_view(), name='details'),
]
