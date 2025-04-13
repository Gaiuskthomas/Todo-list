from django.shortcuts import render, redirect
from .models import ToDo

def index(request):
    tasks = ToDo.objects.all()
    if request.method == 'POST' :
        title = request.POST.get('title')
        print(title)
        ToDo.objects.create(title=title)
        return redirect('index')
    return render(request,'index.html',{'tasks':tasks})
def sample(request):
    return render(request,'sample.html')
# Create your views here.
def update_task(request, task_id):
    if request.method == 'POST' :
        title = request.POST.get('title')
        ToDo.objects.filter(id=task_id).update(title=title)
        return redirect('index')
    else:
        return render(request, 'update.html')
def delete_task(request, task_id):
    ToDo.objects.filter(id=task_id).delete()
    return redirect('index')

