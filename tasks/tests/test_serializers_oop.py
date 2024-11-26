import pytest
from django.utils.timezone import now
from tasks.serializers import TaskSerializer

@pytest.mark.django_db
class TestTaskSerializer:
    def test_valid_serializer_data(self):
        '''Перевірки валідності сериализатора з правильними даними.'''

        valid_data = {
            'title': 'OOP Test Task',
            'description': 'OOP description.',
            'due_date': now().date()
        }
        serializer = TaskSerializer(data=valid_data)
        assert serializer.is_valid()

    def test_missing_title_field(self):
        '''Перевірки помилок сериализатора, якщо заголовок поля обов'язково відсутній.'''

        invalid_data = {
            'description': 'Task without title.',
            'due_date': now().date()
        }
        serializer = TaskSerializer(data=invalid_data)
        assert not serializer.is_valid()
        assert 'title' in serializer.errors

    def test_due_date_in_past(self):
        '''Перевірка того, що дані не можуть бути в минулому'''

        invalid_data = {
            'title': 'OOP Past Task',
            'description': 'OOP task with invalid due date.',
            'due_date': now().date().replace(year=now().year - 1)
        }
        serializer = TaskSerializer(data=invalid_data)
        assert not serializer.is_valid()
        assert 'due_date' in serializer.errors
