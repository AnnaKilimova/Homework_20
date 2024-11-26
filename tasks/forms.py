from django import forms
from django.utils.timezone import now
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < now().date():
            raise forms.ValidationError("Due date cannot be in the past.")
        return due_date
