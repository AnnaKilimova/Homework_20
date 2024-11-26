from rest_framework import serializers
from .models import User, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user, _ = User.objects.get_or_create(**user_data)
        task = Task.objects.create(user=user, **validated_data)
        return task
