#https://www.csestack.org/create-html-form-insert-data-database-django/
#https://www.geeksforgeeks.org/django-modelform-create-form-from-models/

from django import forms
from todolist.models import Task

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
        label = {"title":"Title", "description":"Description"}