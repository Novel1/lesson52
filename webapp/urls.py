from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.index_view),
    path('todolist', views.todolist_view),
    path('add', views.add_view),
]