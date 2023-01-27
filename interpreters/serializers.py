from rest_framework import serializers
from .models import Interpreter


class InterpreterSerializer(serializers.ModelSerializer):
    store_name = serializers.CharField(max_length=19)

    class Meta:
        model = Interpreter
        fields = '__all__'

    def create(self, validated_data):
        return Interpreter.objects.get_or_create(**validated_data)[0]
