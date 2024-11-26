from rest_framework import serializers
from django.utils.timezone import now
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

    def validate_due_date(self, value):
        """
        Перевіряємо, що дата завершення не в минулому.
        """
        if value < now().date():
            raise serializers.ValidationError("The due date cannot be in the past.")
        return value
