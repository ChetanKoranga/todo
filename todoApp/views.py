from django.shortcuts import render
from .models import todo

def home(request):
    all_todo = todo.objects.all()
    context = {'all_todo':all_todo}
    return render(request,'todoApp/index.html',context)

def detail(request,todo_id):
    context = {'current_todo':todo.objects.get(pk=todo_id)}
    return render(request,'todoApp/detail.html',context)