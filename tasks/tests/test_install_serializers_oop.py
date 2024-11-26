from rest_framework.exceptions import ValidationError
from tasks.install_serializer import TaskSerializer
import pytest
from datetime import date


@pytest.mark.django_db
class TestTaskSerializer:

    def test_valid_serializer(self):
        '''Перевіркa валідності сериализатора з правильними внесеними даними.'''

        valid_data = {
            "title": "Task 1",
            "description": "A valid task description",
            "due_date": str(date.today()),
            "user": {
                "username": "validuser",
                "email": "validuser@example.com"
            }
        }
        serializer = TaskSerializer(data=valid_data)
        assert serializer.is_valid()
        task = serializer.save()
        assert task.title == valid_data['title']
        assert task.due_date.isoformat() == valid_data['due_date']
        assert task.user.email == valid_data['user']['email']

    def test_invalid_user_serializer(self):
        '''Помилки перевірки, якщо дані вкладеного сериализатора (користувача) невірні.'''

        invalid_data = {
            "title": "Task 2",
            "description": "Another task description",
            "user": {
                "username": "",
                "email": "not-an-email"
            }
        }
        serializer = TaskSerializer(data=invalid_data)
        with pytest.raises(ValidationError):
            serializer.is_valid(raise_exception=True)
