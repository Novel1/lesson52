from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from webapp.models import ToDo


# Create your views here.
def index_view(request: WSGIRequest):
    return render(request, 'index.html')


def todolist_view(request: WSGIRequest):
    todo = ToDo.objects.all()
    context = {
        'todo': todo
    }
    return render(request, 'todolist.html', context=context)


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'add_todo.html')
    print(request.POST)
    context = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'created_at': request.POST.get('data')
    }
    todo = ToDo.objects.create(**context)
    return redirect(f'/add?pk={todo.pk}')
