from rest_framework import serializers

from .models import Machine
import datetime

# class MachineSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Machine
#         fields = ['id', 'ee_tag', 'alias', 'ip', 'description', 'updated']

class MachineSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ee_tag = serializers.CharField()
    alias = serializers.CharField()
    ip = serializers.CharField(required=True)
    description = serializers.CharField(required=False, allow_blank=True)
    updated = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        '''
        Create and return a new `Machine` instance, given the validated data.
        '''
        return Machine.objects.create(**validated_data)

    def update(self, instance, validated_data):
        '''
        Update and return an existing `Machine` instance, given the validated data.
        '''
        instance.ee_tag = validated_data.get('ee_tag', instance.ee_tag)
        instance.alias = validated_data.get('alias', instance.alias)
        instance.ip = validated_data.get('ip', instance.ip)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
