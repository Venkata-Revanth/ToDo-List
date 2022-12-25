from django.shortcuts import redirect, render
from demo.models import Todo
# Create your views here.


def index(request):
    Todos = Todo.objects.all()
    if request.method == "POST":
        text = request.POST.get('text')
        if(text == ""):
            return render(request, 'demo/index.html', {'Todos': Todos})
        todo = Todo(text=text)
        todo.save()
        return redirect('/')
    return render(request, 'demo/index.html', {'Todos': Todos})


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')


def edit(request):
    if(request.method == "GET"):
        return redirect('/')
    id = request.POST.get("id")
    text = request.POST.get("text")
    todo = Todo.objects.filter(id=id)
    if(todo.exists()):
        todo = todo.first()
        if(text != ""):
            todo.text = text
            todo.save()
    return redirect('/')
