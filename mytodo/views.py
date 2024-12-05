from django.shortcuts import render, redirect
from .forms import todoform
from .models import todo

def base(request):
    return render(request, 'base.html')


def home(request):
    form = todoform(request.POST or None)
    tasks = todo.objects.all()
    if request.method == 'POST' and form.is_valid():
        form.save()  # Save the form directly to the database
        redirect('/home')
    return render(request, 'home.html', {'form': form , 'tasks':tasks })

def delete_task(request, task_id):
    try:
        task = todo.objects.get(id=task_id)
        task.delete()
    except todo.DoesNotExist:
        pass  # Handle missing task

    return redirect('/home') 