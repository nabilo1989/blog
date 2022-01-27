from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages

def say_hello(request):
    all = Todo.objects.all()
    return render(request, 'index.html', {'info': all})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request,'todo deletedt succesfull',extra_tags='success')
    return redirect('home')

# Create your views here.
