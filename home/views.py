from django.shortcuts import render
from .models import Todo




def say_hello(request):
    person={'name':'majid','age':35}
    all = Todo.objects.all()
    return render(request,'index.html',{'info':all})
# Create your views here.
