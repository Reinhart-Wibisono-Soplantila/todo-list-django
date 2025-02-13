from rest_framework import serializers
from .models import ToDo

class ToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model=ToDo
        fields='__all__'
        read_only_fields=['user', 'created_at', 'updated_at']