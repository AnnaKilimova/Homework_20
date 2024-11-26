import pytest
from django.utils.timezone import now
from tasks.forms import TaskForm

@pytest.mark.django_db
def test_valid_form_data():
    '''Перевірка валідності форми з правильними даними.'''

    form_data = {
        'title': 'Test Task',
        'description': 'This is a test task.',
        'due_date': now().date(),
    }
    form = TaskForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_empty_required_fields():
    '''Перевірка помилок при пустих обов’язкових полях.'''

    form_data = {}
    form = TaskForm(data=form_data)
    assert not form.is_valid()
    assert 'title' in form.errors
    assert 'due_date' in form.errors

@pytest.mark.django_db
def test_due_date_in_past():
    '''Перевірка валідації поля дати на неможливість встановлення минулої дати.'''

    form_data = {
        'title': 'Past Due Task',
        'description': 'This task has an invalid due date.',
        'due_date': (now().date().replace(year=now().year - 1)),
    }
    form = TaskForm(data=form_data)
    assert not form.is_valid()
    assert 'due_date' in form.errors
