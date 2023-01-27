from rest_framework import serializers
from .models import File
from interpreters.serializers import InterpreterSerializer
import os
from utils.converter import convert_cnab, read_cnab


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

    def create(self, validated_data):
        file = validated_data.get('file')
        if file.name != 'CNAB.txt':
            raise NameError("Nome deve ser CNAB")

        convert_txt = File.objects.create(**validated_data)
        convert_cnab()

        list_info = read_cnab()
        for info in list_info:
            serializer = InterpreterSerializer(data=info)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        if os.path.isfile('files_up/CNAB.txt'):
            os.remove('files_up/CNAB.txt')
        return convert_txt
