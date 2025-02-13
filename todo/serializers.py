from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ToDo

class ToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model=ToDo
        fields='__all__'
        read_only_fields=['user', 'created_at', 'updated_at']

class RegistrationSerializers(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True, required=True)
    class Meta:
        model=User
        fields=['username', 'email', 'password', 'password2']
        extra_kwargs={'password':{'write_only':True}}
        
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        if password!=password2:
            raise serializers.ValidationError({"password":"Password tidak cocok"})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2', None)
        user=User.objects.create_user(**validated_data)
        return user