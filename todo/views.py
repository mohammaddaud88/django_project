from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task = task, is_completed = False)
    return redirect('home')

def mark_as_done(request,pk):
    # Task.objects.filter(pk=pk).update(is_completed=True)
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def deleteTask(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')

def markAsIncomplete(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def editTask(request,pk):
    task = get_object_or_404(Task,pk=pk)
    context = {'task':task}
    return render(request,'edit_task.html',context)

def updateTask(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.task = request.POST['task']
    task.save()
    return redirect('home')

