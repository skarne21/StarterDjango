from django import forms
from .models import ToDoList, Item
from datetime import date


class CreateNewList(forms.Form):
     name = forms.CharField(label="Name", max_length=200)

class ShowSpecific(forms.Form):
     id = forms.ModelChoiceField(queryset=ToDoList.objects.none())

     def __init__(self, *args, **kwargs):
          user = kwargs.pop('user', None)
          super(ShowSpecific, self).__init__(*args, **kwargs)
          if user:
               self.fields['id'].queryset = ToDoList.objects.filter(user=user)

class NameToGreet(forms.Form):
     name = forms.CharField(label = "Name", max_length=200)

class addToList(forms.Form):
     Task = forms.CharField(label = "Task", max_length=200)
     dueDate = forms.DateField(label = "Due Date ", widget=forms.DateInput(attrs={'type': 'date'}), initial = date.today())
     complete = forms.BooleanField(label = "Completed?", required=False)