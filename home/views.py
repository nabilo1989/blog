from django.shortcuts import render,redirect
from .models import Todo


def say_hello(request):
    person = {'name': 'majid', 'age': 35}
    all = Todo.objects.all()
    return render(request, 'index.html', {'info': all})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})


# Create your views here.
