from django.shortcuts import render


def say_hello(request):
    person={'name':'majid','age':35}
    return render(request,'index.html',context=person)
# Create your views here.
