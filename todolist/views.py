from django.shortcuts import render, redirect
from .models import TodoList, Category
from datetime import datetime


def index(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + " -- " + date + " " + category
            datetime_object = datetime.strptime(date, "%Y-%m-%d")
            Todo = TodoList(title=title, content=content, due_date=datetime_object, category=Category.objects.get(name=category))
            Todo.save()
            return redirect("/")

        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()

    return render(request, "todolist/index.html", {"todos": todos, "categories": categories})

