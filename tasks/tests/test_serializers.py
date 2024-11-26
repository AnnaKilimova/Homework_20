import pytest
from django.utils.timezone import now
from tasks.serializers import TaskSerializer
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_valid_serializer_data():
    '''Перевірки валідності сериализатора з правильними даними.'''

    valid_data = {
        'title': 'Test Task',
        'description': 'This is a test task.',
        'due_date': now().date()
    }
    serializer = TaskSerializer(data=valid_data)
    assert serializer.is_valid()

@pytest.mark.django_db
def test_missing_title_field():
    '''Перевірки помилок сериализатора, якщо заголовок поля обов'язково відсутній.'''

    invalid_data = {
        'description': 'Task without a title.',
        'due_date': now().date()
    }
    serializer = TaskSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert 'title' in serializer.errors

@pytest.mark.django_db
def test_due_date_in_past():
    '''Перевірка того, що дані не можуть бути в минулому'''

    invalid_data = {
        'title': 'Past Task',
        'description': 'Task with a past due date.',
        'due_date': now().date().replace(year=now().year - 1)
    }
    serializer = TaskSerializer(data=invalid_data)
    assert not serializer.is_valid()
    assert 'due_date' in serializer.errors
