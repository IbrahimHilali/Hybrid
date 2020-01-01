from django.urls import path

from Projects import views

app_name = 'Projects'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]
