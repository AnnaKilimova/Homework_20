import pytest
from django.utils.timezone import now
from tasks.forms import TaskForm

@pytest.mark.django_db
class TestTaskForm:
    def test_valid_form(self):
        '''Перевірка валідності форми з правильними даними.'''

        form_data = {
            'title': 'OOP Task',
            'description': 'OOP test description.',
            'due_date': now().date(),
        }
        form = TaskForm(data=form_data)
        assert form.is_valid()

    def test_missing_required_fields(self):
        '''Перевірка помилок при пустих обов’язкових полях.'''

        form_data = {}
        form = TaskForm(data=form_data)
        assert not form.is_valid()
        assert 'title' in form.errors
        assert 'due_date' in form.errors

    def test_due_date_in_past(self):
        '''Перевірка валідації поля дати на неможливість встановлення минулої дати.'''

        form_data = {
            'title': 'OOP Invalid Task',
            'description': 'Task with past due date.',
            'due_date': (now().date().replace(year=now().year - 1)),
        }
        form = TaskForm(data=form_data)
        assert not form.is_valid()
        assert 'due_date' in form.errors
