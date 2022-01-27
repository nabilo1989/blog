from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm, TodoUpdateForm


def say_hello(request):
    all = Todo.objects.all()
    return render(request, 'index.html', {'info': all})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', {'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'todo deletedt succesfull', extra_tags='success')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], email=cd['email'], created=cd['created'])
            messages.success(request, 'To do create succsess', 'success')
            return redirect('home')
    else:
        form = TodoCreateForm()
    return render(request, 'create.html', {'form': form})


def update(request, todo_id):
    todo=Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form= TodoUpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'To do updated succsess', 'success')
            return redirect('detail',todo_id)


    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})
# Create your views here.
