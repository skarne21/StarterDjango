from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList, ShowSpecific, NameToGreet, addToList
# Create your views here.
def home(response):
    if not (response.user.is_authenticated):
        return render(response, "main/home.html", {})
    form1 = form1 = ShowSpecific(user=response.user)
    form2 = NameToGreet()

    if response.method=="POST":
        if response.POST.get('action')=="submit1":
            form1 = ShowSpecific(response.POST)
            if form1.is_valid():
                id = form1.cleaned_data['id']
                return HttpResponseRedirect("/%i" % id.order)
        elif response.POST.get('action')=="submit2":
            form2 = NameToGreet(response.POST)
            if form2.is_valid():
                name = form2.cleaned_data['name']
                return HttpResponseRedirect("/greet/%s" % name)

    return render(response, "main/home.html", {"form1": form1, "form2": form2})





def greet(response, welcome):
    return render(response, "main/base.html", {"name": welcome.capitalize()})

def content(response, id):
    taskForm = addToList()
    
    ls = response.user.todolist_set.filter(order=id).first()
    
    if not ls:
        return render(response, "main/tableList.html", {
            "nameTable": "An Error Has Occured", 
            "nameList": "This list does not exist."
        })

    if response.method == "POST":
        if response.POST.get('save') == "newTask":
            taskForm = addToList(response.POST)
            if taskForm.is_valid():
                taskName = taskForm.cleaned_data['Task']
                completed = taskForm.cleaned_data['complete']
                date = taskForm.cleaned_data['dueDate']
                ls.item_set.create(text=taskName, taskId=ls.item_set.count() + 1, complete=completed, taskDueDate=date)
        else:
            checked_task_ids = response.POST.getlist('toggledItem')
            for item in ls.item_set.all():
                item_id_str = str(item.taskId)
                item.complete = item_id_str in checked_task_ids
                item.save()
                
        return HttpResponseRedirect("/%i" % id)

    sorted_items = ls.item_set.all().order_by('taskDueDate')
    return render(response, "main/tableList.html", {"ls": ls, "sort": sorted_items, "form": taskForm})

def create (response):
    if response.method=="POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = response.user.todolist_set.create(name=n, order = response.user.todolist_set.all().count() + 1)
            t.save()
        return HttpResponseRedirect("/%i" % t.order)

    else:
        form = CreateNewList()
    return render(response, "main/createTable.html",{"form": form})

def showAll(response):
    if not response.user.is_authenticated:
        
        return render(response, 'main/showAll.html', {"all": []})
    user_lists = response.user.todolist_set.all() # Get lists once
    if response.method == "POST":
        idToDelete = response.POST.get("idToDelete")
        user_lists.filter(order=idToDelete).delete()
        reorder(user_lists)
    return render(response, 'main/showAll.html', {"all": user_lists})

def reorder(object):
    size = object.count()
    i=1
    for item in object.all():
        if(i!=item.order):
            item.order=i
            item.save()
        i+=1
