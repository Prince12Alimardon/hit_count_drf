from django.urls import path
from .views import TodoListView, TodoDetailView

urlpatterns = [
    path('todos/', TodoListView.as_view(), name='todo_list'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo_detail'),
]
