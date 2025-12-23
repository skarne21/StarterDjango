from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)
    taskId = models.IntegerField(default=0)
    taskDueDate = models.DateField(default = date.today())
    def __str__(self):
        return self.text