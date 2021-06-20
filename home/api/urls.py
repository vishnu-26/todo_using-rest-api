from django.urls import path,include
from . import views

app_name='api'

urlpatterns = [

#    path('',views.frontend,name="frontend"),
    path('todo-list/', views.todoList, name="todo-list"),
	path('todo-detail/<str:pk>/', views.todoDetail, name="todo-detail"),
	path('todo-create/', views.todoCreate, name="todo-create"),

	path('todo-update/<str:pk>/', views.todoUpdate, name="todo-update"),
	path('todo-delete/<str:pk>/', views.todoDelete, name="todo-delete"),


]
