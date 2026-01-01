from django.shortcuts import render, redirect
from  tasks.models import Task
from django.db.models import Count, Q
from tasks.forms import TaskModelForm, TaskDetailModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def manager_dashboard(request):
    counts = Task.objects.aggregate(
        total=Count('id'),
        completed=Count('id', filter=Q(status='COMPLETED')),
        pending=Count('id', filter=Q(status='PENDING')),
        in_progress=Count('id', filter=Q(status='IN_PROGRESS')),
    )

    filter_type = request.GET.get('type', 'all')
    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')
    if filter_type == 'completed':
        tasks = base_query.filter(status='COMPLETED')
    elif filter_type == 'pending':
        tasks = base_query.filter(status='PENDING')
    elif filter_type == 'in_progress':
        tasks = base_query.filter(status='IN_PROGRESS')
    elif filter_type == 'all':
        tasks = base_query.all()

    context = {
        'counts': counts,
        'tasks': tasks
    }
    return render(request,'dashboard/manager-dashboard.html',context)

def user_dashboard(request):
    return render(request,'dashboard/user-dashboard.html')

def create_task(request):
    task_form = TaskModelForm()
    task_detail_form = TaskDetailModelForm()
    if request.method == 'POST':
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST, request.FILES)
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
            messages.success(request, 'Task created successfully')
            return redirect('create-task')
    context = {
        'task_form': task_form,
        'task_detail_form': task_detail_form
    }
    return render(request, 'task_form.html', context)

@login_required
def task_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'dashboard/task_list.html', context)

def view_task(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task': task
    }
    return render(request, 'view_task.html', context)

def edit_task(request, id):
    task = Task.objects.get(id=id)

    if task.details:
        task_detail_form = TaskDetailModelForm(instance=task.details)
    else:
        task_detail_form = TaskDetailModelForm()

    if request.method == 'POST':
        task_form = TaskModelForm(request.POST, instance=task)
        if task.details:
            task_detail_form = TaskDetailModelForm(request.POST, request.FILES, instance=task.details)
        else:
            task_detail_form = TaskDetailModelForm(request.POST)

        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
            messages.success(request, 'Task updated successfully')
            return redirect('edit-task', id)
    else:
        task_form = TaskModelForm(instance=task)

    context = {
        'task_form': task_form,
        'task_detail_form': task_detail_form
    }
    return render(request, 'task_form.html', context)

def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, 'Task deleted successfully')
        return redirect('manager-dashboard')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('manager-dashboard')