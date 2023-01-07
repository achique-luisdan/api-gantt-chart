from django.urls import path

from . import views

urlpatterns = [
    path('sprints', views.get_sprints),
    path('sprints/<int:sprint_id>', views.get_sprint),
]