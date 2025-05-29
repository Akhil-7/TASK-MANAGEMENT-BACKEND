from django.urls import path
from .views import TaskView, DashboardView
urlpatterns = [
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>/', TaskView.as_view()),
    path('home/', DashboardView.as_view())
]
