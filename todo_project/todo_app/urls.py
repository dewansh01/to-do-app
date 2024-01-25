from django.urls import path
from . import views
urlpatterns=[
    path('',views.greet,name='greet'),
    path('list',views.todo_list,name='todo_list'),
    path('list/<int:id>',views.details,name='details')
]