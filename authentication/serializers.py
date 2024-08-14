from rest_framework import serializers
from .models import User
from .models import TareaEscolar

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class TareaEscolarSerializer(serializers.ModelSerializer):
    advertencia = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = TareaEscolar
        fields = ['id', 'titulo', 'descripcion', 'fecha_entrega', 'completada', 'usuario', 'advertencia']
        read_only_fields = ['usuario', 'advertencia']